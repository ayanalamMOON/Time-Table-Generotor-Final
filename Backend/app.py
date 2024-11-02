from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from csp import generate
from model import Constraint, Course, CreateConstraint, CreateCourse, TimetableAIModel, train_ai_model, predict_timetable, ConstraintTemplate, ConstraintTemplateManager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import motor.motor_asyncio
import uvicorn

client = motor.motor_asyncio.AsyncIOMotorClient(
    'mongodb://localhost:27017/timetable')
database = client.timetable
courses_collection = database.courses
constraints_collection = database.constraints
templates_collection = database.templates

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run("app:app", host="localhost",
                port=8000, reload=True, debug=True)


@app.get("/get-courses")
async def get_courses():
    courses = []
    cursor = courses_collection.find({})
    async for document in cursor:
        courses.append(Course(**document))
    return courses


@app.get("/get-constraints")
async def get_constraints():
    constraints = []
    cursor = constraints_collection.find({})
    async for document in cursor:
        constraints.append(Constraint(**document))
    return constraints


@app.post("/add-course", response_model=Course)
async def post_course(course: CreateCourse):
    document = course.dict()
    await courses_collection.insert_one(document)
    return document


@app.post("/add-constraints", response_model=Constraint)
async def post_constraints(constraint: CreateConstraint):
    document = constraint.dict()
    await constraints_collection.insert_one(document)
    return document


@app.get("/generate-timetable")
async def generate_timetable():
    constraints = []
    cursor = constraints_collection.find({})
    async for document in cursor:
        constraints.append(Constraint(**document))

    courses = []
    cursor = courses_collection.find({})
    async for document in cursor:
        courses.append(Course(**document))

    if constraints == [] or courses == []:
        return HTMLResponse(status_code=400)

    courses = [item.dict() for item in courses]

    # Load historical data in the specified format
    historical_data = [
        {"features": [0.1, 0.2, 0.3], "label": 1},
        {"features": [0.4, 0.5, 0.6], "label": 0}
    ]

    # Use AI model for timetable prediction
    ai_model = train_ai_model(historical_data)

    # Prepare input data in the specified format
    input_data = [0.7, 0.8, 0.9]
    predicted_timetable = predict_timetable(ai_model, input_data)

    data = generate(constraints[-1].dict(), courses)
    return data


class UpdateCourse(BaseModel):
    name: str
    lectureno: int
    duration: int
    instructor_name: str
    start_hr: int
    end_hr: int


@app.put("/update-course/{course_id}", response_model=Course)
async def update_course(course_id: str, course: UpdateCourse):
    document = course.dict()
    result = await courses_collection.update_one({"_id": course_id}, {"$set": document})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Course not found")
    updated_course = await courses_collection.find_one({"_id": course_id})
    return updated_course


@app.post("/add-template", response_model=ConstraintTemplate)
async def add_template(template: ConstraintTemplate):
    document = template.dict()
    await templates_collection.insert_one(document)
    return document


@app.get("/get-templates")
async def get_templates():
    templates = []
    cursor = templates_collection.find({})
    async for document in cursor:
        templates.append(ConstraintTemplate(**document))
    return templates


@app.get("/get-template/{template_id}", response_model=ConstraintTemplate)
async def get_template(template_id: str):
    document = await templates_collection.find_one({"_id": template_id})
    if document is None:
        raise HTTPException(status_code=404, detail="Template not found")
    return ConstraintTemplate(**document)


@app.post("/import-template", response_model=ConstraintTemplate)
async def import_template(template: ConstraintTemplate):
    document = template.dict()
    await templates_collection.insert_one(document)
    return document


@app.get("/export-template/{template_id}", response_model=ConstraintTemplate)
async def export_template(template_id: str):
    document = await templates_collection.find_one({"_id": template_id})
    if document is None:
        raise HTTPException(status_code=404, detail="Template not found")
    return ConstraintTemplate(**document)
