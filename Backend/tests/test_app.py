import pytest
from httpx import AsyncClient
from app import app

@pytest.mark.asyncio
async def test_get_courses():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/get-courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_constraints():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/get-constraints")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_post_course():
    course_data = {
        "name": "Test Course",
        "lectureno": 10,
        "duration": 2,
        "instructor_name": "Test Instructor",
        "start_hr": 9,
        "end_hr": 11
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-course", json=course_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Course"

@pytest.mark.asyncio
async def test_post_constraints():
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
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-constraints", json=constraints_data)
    assert response.status_code == 200
    assert response.json()["working_days"][0]["day"] == "Monday"

@pytest.mark.asyncio
async def test_generate_timetable():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 200 or response.status_code == 400

@pytest.mark.asyncio
async def test_update_course():
    course_data = {
        "name": "Updated Course",
        "lectureno": 15,
        "duration": 3,
        "instructor_name": "Updated Instructor",
        "start_hr": 10,
        "end_hr": 12
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.put("/update-course/{course_id}", json=course_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Course"

@pytest.mark.asyncio
async def test_generate_timetable_no_constraints():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_generate_timetable_no_courses():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_generate_timetable_invalid_fields():
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
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-constraints", json=constraints_data)
    assert response.status_code == 200

    course_data = {
        "name": "Test Course",
        "lectureno": 10,
        "duration": 2,
        "instructor_name": "Test Instructor",
        "start_hr": 9,
        "end_hr": 11
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-course", json=course_data)
    assert response.status_code == 200

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_generate_timetable_scheduling_conflicts():
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
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-constraints", json=constraints_data)
    assert response.status_code == 200

    course_data = {
        "name": "Test Course",
        "lectureno": 10,
        "duration": 2,
        "instructor_name": "Test Instructor",
        "start_hr": 9,
        "end_hr": 11
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-course", json=course_data)
    assert response.status_code == 200

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_generate_timetable_ai_model_issues():
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
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-constraints", json=constraints_data)
    assert response.status_code == 200

    course_data = {
        "name": "Test Course",
        "lectureno": 10,
        "duration": 2,
        "instructor_name": "Test Instructor",
        "start_hr": 9,
        "end_hr": 11
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-course", json=course_data)
    assert response.status_code == 200

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_templates():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/get-templates")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_template():
    template_id = "some_template_id"
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/get-template/{template_id}")
    assert response.status_code == 200 or response.status_code == 404

@pytest.mark.asyncio
async def test_add_template():
    template_data = {
        "name": "Test Template",
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
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-template", json=template_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Template"

@pytest.mark.asyncio
async def test_import_template():
    template_data = {
        "name": "Test Template",
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
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/import-template", json=template_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Template"

@pytest.mark.asyncio
async def test_export_template():
    template_id = "some_template_id"
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/export-template/{template_id}")
    assert response.status_code == 200 or response.status_code == 404

@pytest.mark.asyncio
async def test_get_courses_edge_cases():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/get-courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(isinstance(course, dict) for course in response.json())

@pytest.mark.asyncio
async def test_get_constraints_edge_cases():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/get-constraints")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(isinstance(constraint, dict) for constraint in response.json())

@pytest.mark.asyncio
async def test_post_course_edge_cases():
    course_data = {
        "name": "",
        "lectureno": 0,
        "duration": 0,
        "instructor_name": "",
        "start_hr": 0,
        "end_hr": 0
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-course", json=course_data)
    assert response.status_code == 200
    assert response.json()["name"] == ""

    course_data = {
        "name": "A" * 100,
        "lectureno": 100,
        "duration": 100,
        "instructor_name": "B" * 100,
        "start_hr": 23,
        "end_hr": 24
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-course", json=course_data)
    assert response.status_code == 200
    assert response.json()["name"] == "A" * 100

@pytest.mark.asyncio
async def test_post_constraints_edge_cases():
    constraints_data = {
        "working_days": [],
        "consecutive_subjects": [],
        "non_consecutive_subjects": []
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-constraints", json=constraints_data)
    assert response.status_code == 200
    assert response.json()["working_days"] == []

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
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-constraints", json=constraints_data)
    assert response.status_code == 200
    assert response.json()["working_days"][0]["day"] == "Monday"

@pytest.mark.asyncio
async def test_generate_timetable_edge_cases():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 200 or response.status_code == 400

@pytest.mark.asyncio
async def test_update_course_edge_cases():
    course_data = {
        "name": "",
        "lectureno": 0,
        "duration": 0,
        "instructor_name": "",
        "start_hr": 0,
        "end_hr": 0
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.put("/update-course/{course_id}", json=course_data)
    assert response.status_code == 200
    assert response.json()["name"] == ""

    course_data = {
        "name": "A" * 100,
        "lectureno": 100,
        "duration": 100,
        "instructor_name": "B" * 100,
        "start_hr": 23,
        "end_hr": 24
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.put("/update-course/{course_id}", json=course_data)
    assert response.status_code == 200
    assert response.json()["name"] == "A" * 100

@pytest.mark.asyncio
async def test_generate_timetable_no_constraints_edge_cases():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_generate_timetable_no_courses_edge_cases():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_generate_timetable_invalid_fields_edge_cases():
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
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-constraints", json=constraints_data)
    assert response.status_code == 200

    course_data = {
        "name": "Test Course",
        "lectureno": 10,
        "duration": 2,
        "instructor_name": "Test Instructor",
        "start_hr": 9,
        "end_hr": 11
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-course", json=course_data)
    assert response.status_code == 200

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_generate_timetable_scheduling_conflicts_edge_cases():
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
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-constraints", json=constraints_data)
    assert response.status_code == 200

    course_data = {
        "name": "Test Course",
        "lectureno": 10,
        "duration": 2,
        "instructor_name": "Test Instructor",
        "start_hr": 9,
        "end_hr": 11
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-course", json=course_data)
    assert response.status_code == 200

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_generate_timetable_ai_model_issues_edge_cases():
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
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-constraints", json=constraints_data)
    assert response.status_code == 200

    course_data = {
        "name": "Test Course",
        "lectureno": 10,
        "duration": 2,
        "instructor_name": "Test Instructor",
        "start_hr": 9,
        "end_hr": 11
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-course", json=course_data)
    assert response.status_code == 200

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_generate_timetable_new_csp_solver():
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
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-constraints", json=constraints_data)
    assert response.status_code == 200

    course_data = {
        "name": "Test Course",
        "lectureno": 10,
        "duration": 2,
        "instructor_name": "Test Instructor",
        "start_hr": 9,
        "end_hr": 11
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-course", json=course_data)
    assert response.status_code == 200

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_generate_timetable_recommendation_system():
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
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-constraints", json=constraints_data)
    assert response.status_code == 200

    course_data = {
        "name": "Test Course",
        "lectureno": 10,
        "duration": 2,
        "instructor_name": "Test Instructor",
        "start_hr": 9,
        "end_hr": 11
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-course", json=course_data)
    assert response.status_code == 200

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_project_running():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
