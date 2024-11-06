from typing import List, Dict, Any
from pydantic import BaseModel, Field
from bson import ObjectId
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout, Bidirectional
from tensorflow.keras.optimizers import Adam, RMSprop
from tensorflow.keras.callbacks import EarlyStopping
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import BaggingRegressor, GradientBoostingRegressor, StackingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from skopt import BayesSearchCV


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> ObjectId:
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)  # pragma: no cover
    
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type="string")


class CreateCourse(BaseModel):
    name: str
    lectureno: int
    duration: int
    instructor_name: str
    start_hr: int
    end_hr: int


class Course(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
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
    room_availability: Dict[str, List[int]] = None
    teacher_preferences: Dict[str, List[int]] = None
    student_preferences: Dict[str, List[int]] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class Constraints(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    working_days: List[WorkingDay]
    consecutive_subjects: List[str]
    non_consecutive_subjects: List[str]
    room_availability: Dict[str, List[int]] = None
    teacher_preferences: Dict[str, List[int]] = None
    student_preferences: Dict[str, List[int]] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ConstraintTemplate(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    working_days: List[WorkingDay]
    consecutive_subjects: List[str]
    non_consecutive_subjects: List[str]
    room_availability: Dict[str, List[int]] = None
    teacher_preferences: Dict[str, List[int]] = None
    student_preferences: Dict[str, List[int]] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class TimetableAIModel:
    def __init__(self, optimizer: str = 'adam'):
        self.model = Sequential()
        self.model.add(Bidirectional(LSTM(100, return_sequences=True, input_shape=(10, 1))))
        self.model.add(Dropout(0.2))
        self.model.add(Bidirectional(LSTM(100, return_sequences=False)))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(50))
        self.model.add(Dense(1))
        if optimizer == 'adam':
            self.model.compile(optimizer=Adam(), loss='mean_squared_error')
        elif optimizer == 'rmsprop':
            self.model.compile(optimizer=RMSprop(), loss='mean_squared_error')

    def train(self, X_train: np.ndarray, y_train: np.ndarray, epochs: int = 20, batch_size: int = 64) -> None:
        early_stopping = EarlyStopping(monitor='loss', patience=5)
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, callbacks=[early_stopping])

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        return self.model.predict(X_test)


def train_ai_model(historical_data: List[Dict[str, Any]]) -> TimetableAIModel:
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

    # Hyperparameter tuning using Bayesian optimization
    param_space = {
        'batch_size': [32, 64, 128],
        'epochs': [10, 20, 30]
    }
    bayes_search = BayesSearchCV(estimator=model, search_spaces=param_space, n_iter=10, cv=3)
    bayes_search.fit(X_train, y_train)
    best_params = bayes_search.best_params_
    print(f"Best Hyperparameters: {best_params}")

    # Ensemble learning using stacking
    base_learners = [
        ('lr', LinearRegression()),
        ('svr', SVR())
    ]
    stack_model = StackingRegressor(estimators=base_learners, final_estimator=GradientBoostingRegressor())
    stack_model.fit(X_train, y_train)

    return model


def predict_timetable(model: TimetableAIModel, input_data: List[float]) -> np.ndarray:
    X_test = np.array([input_data])
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))  # Reshape for LSTM input
    predictions = model.predict(X_test)

    # Calculate performance metrics
    mse = mean_squared_error(input_data, predictions)
    mae = mean_absolute_error(input_data, predictions)
    rmse = np.sqrt(mse)

    print(f"Prediction Performance - MSE: {mse}, MAE: {mae}, RMSE: {rmse}")

    return predictions


class ConstraintTemplateManager:
    def __init__(self) -> None:
        self.templates = []

    def save_template(self, template: ConstraintTemplate) -> None:
        self.templates.append(template)

    def get_template(self, template_id: str) -> ConstraintTemplate:
        for template in self.templates:
            if str(template.id) == template_id:
                return template
        return None

    def get_all_templates(self) -> List[ConstraintTemplate]:
        return self.templates

    def import_template(self, template: ConstraintTemplate) -> None:
        self.templates.append(template)

    def export_template(self, template_id: str) -> ConstraintTemplate:
        for template in self.templates:
            if str(template.id) == template_id:
                return template
        return None
