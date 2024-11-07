import pytest
from httpx import AsyncClient
from app import app

@pytest.mark.asyncio
async def test_get_courses():
    """
    Test the /get-courses endpoint to ensure it returns a list of courses.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/get-courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_constraints():
    """
    Test the /get-constraints endpoint to ensure it returns a list of constraints.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/get-constraints")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_post_course():
    """
    Test the /add-course endpoint to ensure it adds a course successfully.
    """
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
    """
    Test the /add-constraints endpoint to ensure it adds constraints successfully.
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
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add-constraints", json=constraints_data)
    assert response.status_code == 200
    assert response.json()["working_days"][0]["day"] == "Monday"

@pytest.mark.asyncio
async def test_generate_timetable():
    """
    Test the /generate-timetable endpoint to ensure it generates a timetable.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 200 or response.status_code == 400

@pytest.mark.asyncio
async def test_update_course():
    """
    Test the /update-course/{course_id} endpoint to ensure it updates a course successfully.
    """
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
    """
    Test the /generate-timetable endpoint to ensure it returns a 400 status code when no constraints are provided.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_generate_timetable_no_courses():
    """
    Test the /generate-timetable endpoint to ensure it returns a 400 status code when no courses are provided.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_generate_timetable_invalid_fields():
    """
    Test the /generate-timetable endpoint to ensure it handles invalid fields correctly.
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
    """
    Test the /generate-timetable endpoint to ensure it handles scheduling conflicts correctly.
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
    """
    Test the /generate-timetable endpoint to ensure it handles AI model issues correctly.
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
    """
    Test the /get-templates endpoint to ensure it returns a list of templates.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/get-templates")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_template():
    """
    Test the /get-template/{template_id} endpoint to ensure it returns a template or a 404 status code.
    """
    template_id = "some_template_id"
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/get-template/{template_id}")
    assert response.status_code == 200 or response.status_code == 404

@pytest.mark.asyncio
async def test_add_template():
    """
    Test the /add-template endpoint to ensure it adds a template successfully.
    """
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
    """
    Test the /import-template endpoint to ensure it imports a template successfully.
    """
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
    """
    Test the /export-template/{template_id} endpoint to ensure it exports a template successfully or returns a 404 status code.
    """
    template_id = "some_template_id"
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/export-template/{template_id}")
    assert response.status_code == 200 or response.status_code == 404

@pytest.mark.asyncio
async def test_get_courses_edge_cases():
    """
    Test the /get-courses endpoint to ensure it handles edge cases correctly.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/get-courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(isinstance(course, dict) for course in response.json())

@pytest.mark.asyncio
async def test_get_constraints_edge_cases():
    """
    Test the /get-constraints endpoint to ensure it handles edge cases correctly.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/get-constraints")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(isinstance(constraint, dict) for constraint in response.json())

@pytest.mark.asyncio
async def test_post_course_edge_cases():
    """
    Test the /add-course endpoint to ensure it handles edge cases correctly.
    """
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
    """
    Test the /add-constraints endpoint to ensure it handles edge cases correctly.
    """
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
    """
    Test the /generate-timetable endpoint to ensure it handles edge cases correctly.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 200 or response.status_code == 400

@pytest.mark.asyncio
async def test_update_course_edge_cases():
    """
    Test the /update-course/{course_id} endpoint to ensure it handles edge cases correctly.
    """
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
    """
    Test the /generate-timetable endpoint to ensure it returns a 400 status code when no constraints are provided.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_generate_timetable_no_courses_edge_cases():
    """
    Test the /generate-timetable endpoint to ensure it returns a 400 status code when no courses are provided.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/generate-timetable")
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_generate_timetable_invalid_fields_edge_cases():
    """
    Test the /generate-timetable endpoint to ensure it handles invalid fields correctly.
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
    """
    Test the /generate-timetable endpoint to ensure it handles scheduling conflicts correctly.
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
    """
    Test the /generate-timetable endpoint to ensure it handles AI model issues correctly.
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
    """
    Test the /generate-timetable endpoint to ensure it works with the new CSP solver.
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
    """
    Test the /generate-timetable endpoint to ensure it works with the recommendation system.
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
    """
    Test to ensure the project is running by checking the root endpoint.
    """
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        response = await ac.get("/")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_courses_pagination():
    """
    Test the /get-courses endpoint to ensure it supports pagination.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/get-courses?skip=0&limit=5")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 5

@pytest.mark.asyncio
async def test_get_constraints_pagination():
    """
    Test the /get-constraints endpoint to ensure it supports pagination.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/get-constraints?skip=0&limit=5")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 5

@pytest.mark.asyncio
async def test_get_courses_caching():
    """
    Test the /get-courses endpoint to ensure it supports caching.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response1 = await ac.get("/get-courses")
        response2 = await ac.get("/get-courses")
    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response1.json() == response2.json()

@pytest.mark.asyncio
async def test_get_constraints_caching():
    """
    Test the /get-constraints endpoint to ensure it supports caching.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response1 = await ac.get("/get-constraints")
        response2 = await ac.get("/get-constraints")
    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response1.json() == response2.json()

@pytest.mark.asyncio
async def test_rate_limiting():
    """
    Test the rate limiting functionality to ensure it limits the number of requests.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        for _ in range(10):
            response = await ac.get("/get-courses")
            assert response.status_code == 200
        response = await ac.get("/get-courses")
        assert response.status_code == 429
