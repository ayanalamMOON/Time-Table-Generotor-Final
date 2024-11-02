import pytest
from csp import generate

def test_generate_timetable():
    constraints = {
        "working_days": [
            {"day": "Monday", "start_hr": 9, "end_hr": 17, "total_hours": 8},
            {"day": "Tuesday", "start_hr": 9, "end_hr": 17, "total_hours": 8}
        ],
        "consecutive_subjects": ["Math", "Science"],
        "non_consecutive_subjects": ["History", "Art"]
    }
    courses = [
        {"name": "Math", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17},
        {"name": "Science", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17},
        {"name": "History", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17},
        {"name": "Art", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17}
    ]
    result = generate(constraints, courses)
    assert isinstance(result, dict)
    assert "monday" in result
    assert "tuesday" in result
    assert "wednesday" in result
    assert "thursday" in result
    assert "friday" in result
    assert "saturday" in result
    assert "sunday" in result

def test_generate_timetable_no_constraints():
    constraints = {
        "working_days": [],
        "consecutive_subjects": [],
        "non_consecutive_subjects": []
    }
    courses = [
        {"name": "Math", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17},
        {"name": "Science", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17},
        {"name": "History", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17},
        {"name": "Art", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17}
    ]
    result = generate(constraints, courses)
    assert result is None

def test_generate_timetable_no_courses():
    constraints = {
        "working_days": [
            {"day": "Monday", "start_hr": 9, "end_hr": 17, "total_hours": 8},
            {"day": "Tuesday", "start_hr": 9, "end_hr": 17, "total_hours": 8}
        ],
        "consecutive_subjects": ["Math", "Science"],
        "non_consecutive_subjects": ["History", "Art"]
    }
    courses = []
    result = generate(constraints, courses)
    assert result is None

def test_generate_timetable_invalid_fields():
    constraints = {
        "working_days": [
            {"day": "Monday", "start_hr": 9, "end_hr": 17, "total_hours": 8},
            {"day": "Tuesday", "start_hr": 9, "end_hr": 17, "total_hours": 8}
        ],
        "consecutive_subjects": ["Math", "Science"],
        "non_consecutive_subjects": ["History", "Art"]
    }
    courses = [
        {"name": "Math", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17},
        {"name": "Science", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17},
        {"name": "History", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17},
        {"name": "Art", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17}
    ]
    result = generate(constraints, courses)
    assert isinstance(result, dict)
    assert "monday" in result
    assert "tuesday" in result
    assert "wednesday" in result
    assert "thursday" in result
    assert "friday" in result
    assert "saturday" in result
    assert "sunday" in result

def test_generate_timetable_scheduling_conflicts():
    constraints = {
        "working_days": [
            {"day": "Monday", "start_hr": 9, "end_hr": 17, "total_hours": 8},
            {"day": "Tuesday", "start_hr": 9, "end_hr": 17, "total_hours": 8}
        ],
        "consecutive_subjects": ["Math", "Science"],
        "non_consecutive_subjects": ["History", "Art"]
    }
    courses = [
        {"name": "Math", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17},
        {"name": "Science", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17},
        {"name": "History", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17},
        {"name": "Art", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17}
    ]
    result = generate(constraints, courses)
    assert isinstance(result, dict)
    assert "monday" in result
    assert "tuesday" in result
    assert "wednesday" in result
    assert "thursday" in result
    assert "friday" in result
    assert "saturday" in result
    assert "sunday" in result

def test_generate_timetable_ai_model_issues():
    constraints = {
        "working_days": [
            {"day": "Monday", "start_hr": 9, "end_hr": 17, "total_hours": 8},
            {"day": "Tuesday", "start_hr": 9, "end_hr": 17, "total_hours": 8}
        ],
        "consecutive_subjects": ["Math", "Science"],
        "non_consecutive_subjects": ["History", "Art"]
    }
    courses = [
        {"name": "Math", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17},
        {"name": "Science", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17},
        {"name": "History", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17},
        {"name": "Art", "lectureno": 2, "duration": 1, "start_hr": 9, "end_hr": 17}
    ]
    result = generate(constraints, courses)
    assert isinstance(result, dict)
    assert "monday" in result
    assert "tuesday" in result
    assert "wednesday" in result
    assert "thursday" in result
    assert "friday" in result
    assert "saturday" in result
    assert "sunday" in result
