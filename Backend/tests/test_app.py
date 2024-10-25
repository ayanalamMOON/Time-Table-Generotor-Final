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
