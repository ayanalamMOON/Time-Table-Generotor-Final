import pytest
from model import CreateCourse, Course, CreateConstraints, Constraints, TimetableAIModel, train_ai_model, predict_timetable
import numpy as np

def test_create_course():
    course_data = {
        "name": "Test Course",
        "lectureno": 10,
        "duration": 2,
        "instructor_name": "Test Instructor",
        "start_hr": 9,
        "end_hr": 11
    }
    course = CreateCourse(**course_data)
    assert course.name == "Test Course"
    assert course.lectureno == 10
    assert course.duration == 2
    assert course.instructor_name == "Test Instructor"
    assert course.start_hr == 9
    assert course.end_hr == 11

def test_course():
    course_data = {
        "name": "Test Course",
        "lectureno": 10,
        "duration": 2,
        "instructor_name": "Test Instructor",
        "start_hr": 9,
        "end_hr": 11
    }
    course = Course(**course_data)
    assert course.name == "Test Course"
    assert course.lectureno == 10
    assert course.duration == 2
    assert course.instructor_name == "Test Instructor"
    assert course.start_hr == 9
    assert course.end_hr == 11

def test_create_constraints():
    constraints_data = {
        "working_days": [
            {
                "day": "Monday",
                "start_hr": 9,
                "end_hr": 17,
                "total_hours": 8
            }
        ],
        "consecutive_subjects": ["Math", "Science"],
        "non_consecutive_subjects": ["History", "Art"]
    }
    constraints = CreateConstraints(**constraints_data)
    assert constraints.working_days[0].day == "Monday"
    assert constraints.working_days[0].start_hr == 9
    assert constraints.working_days[0].end_hr == 17
    assert constraints.working_days[0].total_hours == 8
    assert constraints.consecutive_subjects == ["Math", "Science"]
    assert constraints.non_consecutive_subjects == ["History", "Art"]

def test_constraints():
    constraints_data = {
        "working_days": [
            {
                "day": "Monday",
                "start_hr": 9,
                "end_hr": 17,
                "total_hours": 8
            }
        ],
        "consecutive_subjects": ["Math", "Science"],
        "non_consecutive_subjects": ["History", "Art"]
    }
    constraints = Constraints(**constraints_data)
    assert constraints.working_days[0].day == "Monday"
    assert constraints.working_days[0].start_hr == 9
    assert constraints.working_days[0].end_hr == 17
    assert constraints.working_days[0].total_hours == 8
    assert constraints.consecutive_subjects == ["Math", "Science"]
    assert constraints.non_consecutive_subjects == ["History", "Art"]

def test_timetable_ai_model():
    model = TimetableAIModel()
    assert model.model is not None

def test_train_ai_model():
    historical_data = [
        {"features": np.array([1, 2, 3]), "label": 1},
        {"features": np.array([4, 5, 6]), "label": 0}
    ]
    model = train_ai_model(historical_data)
    assert model is not None

def test_predict_timetable():
    model = TimetableAIModel()
    input_data = np.array([1, 2, 3])
    predictions = predict_timetable(model, input_data)
    assert predictions is not None
