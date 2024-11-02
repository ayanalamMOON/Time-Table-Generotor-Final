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

def test_create_course_edge_cases():
    # Test with minimum values
    course_data = {
        "name": "",
        "lectureno": 0,
        "duration": 0,
        "instructor_name": "",
        "start_hr": 0,
        "end_hr": 0
    }
    course = CreateCourse(**course_data)
    assert course.name == ""
    assert course.lectureno == 0
    assert course.duration == 0
    assert course.instructor_name == ""
    assert course.start_hr == 0
    assert course.end_hr == 0

    # Test with maximum values
    course_data = {
        "name": "A" * 100,
        "lectureno": 100,
        "duration": 100,
        "instructor_name": "B" * 100,
        "start_hr": 23,
        "end_hr": 24
    }
    course = CreateCourse(**course_data)
    assert course.name == "A" * 100
    assert course.lectureno == 100
    assert course.duration == 100
    assert course.instructor_name == "B" * 100
    assert course.start_hr == 23
    assert course.end_hr == 24

def test_course_edge_cases():
    # Test with minimum values
    course_data = {
        "name": "",
        "lectureno": 0,
        "duration": 0,
        "instructor_name": "",
        "start_hr": 0,
        "end_hr": 0
    }
    course = Course(**course_data)
    assert course.name == ""
    assert course.lectureno == 0
    assert course.duration == 0
    assert course.instructor_name == ""
    assert course.start_hr == 0
    assert course.end_hr == 0

    # Test with maximum values
    course_data = {
        "name": "A" * 100,
        "lectureno": 100,
        "duration": 100,
        "instructor_name": "B" * 100,
        "start_hr": 23,
        "end_hr": 24
    }
    course = Course(**course_data)
    assert course.name == "A" * 100
    assert course.lectureno == 100
    assert course.duration == 100
    assert course.instructor_name == "B" * 100
    assert course.start_hr == 23
    assert course.end_hr == 24

def test_create_constraints_edge_cases():
    # Test with minimum values
    constraints_data = {
        "working_days": [],
        "consecutive_subjects": [],
        "non_consecutive_subjects": []
    }
    constraints = CreateConstraints(**constraints_data)
    assert constraints.working_days == []
    assert constraints.consecutive_subjects == []
    assert constraints.non_consecutive_subjects == []

    # Test with maximum values
    constraints_data = {
        "working_days": [
            {
                "day": "Monday",
                "start_hr": 0,
                "end_hr": 24,
                "total_hours": 24
            }
        ],
        "consecutive_subjects": ["A" * 100, "B" * 100],
        "non_consecutive_subjects": ["C" * 100, "D" * 100]
    }
    constraints = CreateConstraints(**constraints_data)
    assert constraints.working_days[0].day == "Monday"
    assert constraints.working_days[0].start_hr == 0
    assert constraints.working_days[0].end_hr == 24
    assert constraints.working_days[0].total_hours == 24
    assert constraints.consecutive_subjects == ["A" * 100, "B" * 100]
    assert constraints.non_consecutive_subjects == ["C" * 100, "D" * 100]

def test_constraints_edge_cases():
    # Test with minimum values
    constraints_data = {
        "working_days": [],
        "consecutive_subjects": [],
        "non_consecutive_subjects": []
    }
    constraints = Constraints(**constraints_data)
    assert constraints.working_days == []
    assert constraints.consecutive_subjects == []
    assert constraints.non_consecutive_subjects == []

    # Test with maximum values
    constraints_data = {
        "working_days": [
            {
                "day": "Monday",
                "start_hr": 0,
                "end_hr": 24,
                "total_hours": 24
            }
        ],
        "consecutive_subjects": ["A" * 100, "B" * 100],
        "non_consecutive_subjects": ["C" * 100, "D" * 100]
    }
    constraints = Constraints(**constraints_data)
    assert constraints.working_days[0].day == "Monday"
    assert constraints.working_days[0].start_hr == 0
    assert constraints.working_days[0].end_hr == 24
    assert constraints.working_days[0].total_hours == 24
    assert constraints.consecutive_subjects == ["A" * 100, "B" * 100]
    assert constraints.non_consecutive_subjects == ["C" * 100, "D" * 100]

def test_timetable_ai_model_edge_cases():
    # Test with different optimizers
    model_adam = TimetableAIModel(optimizer='adam')
    assert model_adam.model is not None

    model_rmsprop = TimetableAIModel(optimizer='rmsprop')
    assert model_rmsprop.model is not None

def test_train_ai_model_edge_cases():
    # Test with empty historical data
    historical_data = []
    model = train_ai_model(historical_data)
    assert model is not None

    # Test with large historical data
    historical_data = [
        {"features": np.random.rand(10), "label": np.random.randint(2)}
        for _ in range(1000)
    ]
    model = train_ai_model(historical_data)
    assert model is not None

def test_predict_timetable_edge_cases():
    model = TimetableAIModel()

    # Test with empty input data
    input_data = np.array([])
    predictions = predict_timetable(model, input_data)
    assert predictions is not None

    # Test with large input data
    input_data = np.random.rand(100)
    predictions = predict_timetable(model, input_data)
    assert predictions is not None
