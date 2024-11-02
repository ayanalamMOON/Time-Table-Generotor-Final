from typing import List
from pydantic import BaseModel, Field
from bson import ObjectId
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)  # pragma: no cover
    
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class CreateCourse(BaseModel):
    name: str
    lectureno : int 
    duration : int 
    instructor_name: str
    start_hr: int
    end_hr: int


class Course(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias ="_id")
    name: str
    lectureno: int
    duration: int
    instructor_name: str
    start_hr: int
    end_hr: int

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class WorkingDay(BaseModel):
    day: str
    start_hr: int
    end_hr: int
    total_hours: int


class CreateConstraints(BaseModel):
    working_days: List[WorkingDay]
    consecutive_subjects: List[str]
    non_consecutive_subjects: List[str]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class Constraints(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    working_days: List[WorkingDay]
    consecutive_subjects: List[str]
    non_consecutive_subjects: List[str]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class TimetableAIModel:
    def __init__(self):
        self.model = Sequential()
        self.model.add(LSTM(100, return_sequences=True, input_shape=(10, 1)))
        self.model.add(Dropout(0.2))
        self.model.add(LSTM(100, return_sequences=False))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(50))
        self.model.add(Dense(1))
        self.model.compile(optimizer='adam', loss='mean_squared_error')

    def train(self, X_train, y_train, epochs=20, batch_size=64):
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

    def predict(self, X_test):
        return self.model.predict(X_test)


def train_ai_model(historical_data):
    model = TimetableAIModel()
    X_train = np.array([data['features'] for data in historical_data])
    y_train = np.array([data['label'] for data in historical_data])
    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))  # Reshape for LSTM input
    model.train(X_train, y_train)

    # Calculate performance metrics
    y_pred = model.predict(X_train)
    mse = mean_squared_error(y_train, y_pred)
    mae = mean_absolute_error(y_train, y_pred)
    rmse = np.sqrt(mse)

    print(f"Training Performance - MSE: {mse}, MAE: {mae}, RMSE: {rmse}")

    return model


def predict_timetable(model, input_data):
    X_test = np.array([input_data])
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))  # Reshape for LSTM input
    predictions = model.predict(X_test)

    # Calculate performance metrics
    mse = mean_squared_error(input_data, predictions)
    mae = mean_absolute_error(input_data, predictions)
    rmse = np.sqrt(mse)

    print(f"Prediction Performance - MSE: {mse}, MAE: {mae}, RMSE: {rmse}")

    return predictions
