import pytest
from model import CreateCourse, Course, CreateConstraints, Constraints, TimetableAIModel, train_ai_model, predict_timetable, commit_timetable, get_commits, get_commit, merge_commits, branch_commit
import numpy as np

def test_create_course():
    """
    Test the creation of a course using the CreateCourse model.
    """
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
    """
    Test the creation of a course using the Course model.
    """
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
    """
    Test the creation of constraints using the CreateConstraints model.
    """
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
    """
    Test the creation of constraints using the Constraints model.
    """
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
    """
    Test the creation of the TimetableAIModel.
    """
    model = TimetableAIModel()
    assert model.model is not None

def test_train_ai_model():
    """
    Test the training of the AI model using historical data.
    """
    historical_data = [
        {"features": np.array([1, 2, 3]), "label": 1},
        {"features": np.array([4, 5, 6]), "label": 0}
    ]
    model = train_ai_model(historical_data)
    assert model is not None

def test_predict_timetable():
    """
    Test the prediction of the timetable using the AI model.
    """
    model = TimetableAIModel()
    input_data = np.array([1, 2, 3])
    predictions = predict_timetable(model, input_data)
    assert predictions is not None

def test_create_course_edge_cases():
    """
    Test the creation of a course using the CreateCourse model with edge cases.
    """
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
    """
    Test the creation of a course using the Course model with edge cases.
    """
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
    """
    Test the creation of constraints using the CreateConstraints model with edge cases.
    """
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
    """
    Test the creation of constraints using the Constraints model with edge cases.
    """
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
    """
    Test the creation of the TimetableAIModel with different optimizers.
    """
    # Test with different optimizers
    model_adam = TimetableAIModel(optimizer='adam')
    assert model_adam.model is not None

    model_rmsprop = TimetableAIModel(optimizer='rmsprop')
    assert model_rmsprop.model is not None

def test_train_ai_model_edge_cases():
    """
    Test the training of the AI model using edge cases in historical data.
    """
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
    """
    Test the prediction of the timetable using edge cases in input data.
    """
    model = TimetableAIModel()

    # Test with empty input data
    input_data = np.array([])
    predictions = predict_timetable(model, input_data)
    assert predictions is not None

    # Test with large input data
    input_data = np.random.rand(100)
    predictions = predict_timetable(model, input_data)
    assert predictions is not None

def test_train_ai_model_improved_lstm():
    """
    Test the training of the AI model using improved LSTM architecture.
    """
    historical_data = [
        {"features": np.array([1, 2, 3]), "label": 1},
        {"features": np.array([4, 5, 6]), "label": 0}
    ]
    model = train_ai_model(historical_data)
    assert model is not None

def test_train_ai_model_additional_features():
    """
    Test the training of the AI model using additional features in historical data.
    """
    historical_data = [
        {"features": np.array([1, 2, 3, 4, 5]), "label": 1},
        {"features": np.array([6, 7, 8, 9, 10]), "label": 0}
    ]
    model = train_ai_model(historical_data)
    assert model is not None

def test_recommendation_system():
    """
    Test the recommendation system using the AI model.
    """
    historical_data = [
        {"features": np.array([1, 2, 3]), "label": 1},
        {"features": np.array([4, 5, 6]), "label": 0}
    ]
    model = train_ai_model(historical_data)
    input_data = np.array([1, 2, 3])
    recommendations = predict_timetable(model, input_data)
    assert recommendations is not None

def test_commit_timetable():
    """
    Test the creation of a new timetable commit.
    """
    timetable_data = {
        "courses": [
            {
                "name": "Test Course",
                "lectureno": 10,
                "duration": 2,
                "instructor_name": "Test Instructor",
                "start_hr": 9,
                "end_hr": 11
            }
        ],
        "constraints": {
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
    }
    commit = commit_timetable(timetable_data, "Test User")
    assert commit is not None
    assert commit.user == "Test User"

def test_get_commits():
    """
    Test the retrieval of all timetable commits.
    """
    commits = get_commits()
    assert commits is not None
    assert isinstance(commits, list)

def test_get_commit():
    """
    Test the retrieval of a specific commit by ID.
    """
    commit_id = "some_commit_id"
    commit = get_commit(commit_id)
    assert commit is not None
    assert commit.commit_id == commit_id

def test_merge_commits():
    """
    Test the merging of two timetable commits.
    """
    commit_id_1 = "commit_id_1"
    commit_id_2 = "commit_id_2"
    merged_commit = merge_commits(commit_id_1, commit_id_2, "Test User")
    assert merged_commit is not None
    assert merged_commit.user == "Test User"

def test_branch_commit():
    """
    Test the creation of a new branch from a commit.
    """
    commit_id = "some_commit_id"
    branch_name = "new_branch"
    branch = branch_commit(commit_id, branch_name)
    assert branch is not None
    assert branch.name == branch_name
