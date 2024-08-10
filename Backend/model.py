from typing import List
from pydantic import BaseModel, Field
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls)
        yield cls.validate

    @clssmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)  # pragma: no cover
    
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class CeateCourse(BaseModel):
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
    satrt_hr: int
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
    id: PyObjectId = Field(default_factory=PyObjectId. alias="_id")
    working_days: List[WorkingDay]
    consecutive_subjects: List[str]
    non_consecutive_subjects: List[str]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
