from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from csp import generate
from model import Constraint, Course, CreateConstraint, CreateCourse, TimetableAIModel, train_ai_model, predict_timetable, ConstraintTemplate, ConstraintTemplateManager
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import motor.motor_asyncio
import uvicorn.run
import os
import logging
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional, List
from aiocache import cached
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from starlette.middleware.gzip import GZipMiddleware
import aioredis

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Get the MongoDB connection string from environment variables
MONGODB_CONNECTION_STRING = os.getenv('MONGODB_CONNECTION_STRING', 'mongodb://localhost:27017/timetable')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_CONNECTION_STRING)
database = client.timetable
courses_collection = database.courses
constraints_collection = database.constraints
templates_collection = database.templates
users_collection = database.users

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

app.add_middleware(GZipMiddleware, minimum_size=1000)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Security settings
SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify if the plain password matches the hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Hash the given password.
    """
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT access token with the given data and expiration delta.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_user(username: str) -> Optional[dict]:
    """
    Retrieve a user from the database by username.
    """
    user = await users_collection.find_one({"username": username})
    return user

async def authenticate_user(username: str, password: str) -> Optional[dict]:
    """
    Authenticate a user by username and password.
    """
    user = await get_user(username)
    if not user:
        return None
    if not verify_password(password, user["hashed_password"]):
        return None
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """
    Retrieve the current user based on the provided JWT token.
    """
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await get_user(username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: dict = Depends(get_current_user)) -> dict:
    """
    Retrieve the current active user.
    """
    if current_user["disabled"]:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

async def get_current_admin_user(current_user: dict = Depends(get_current_user)) -> dict:
    """
    Retrieve the current admin user.
    """
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return current_user

class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    role: str

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    password: str
    role: str

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    """
    Endpoint for user login and access token generation.
    """
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/register", response_model=User)
async def register_user(user: UserCreate) -> User:
    """
    Endpoint for user registration.
    """
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict["hashed_password"] = hashed_password
    del user_dict["password"]
    await users_collection.insert_one(user_dict)
    return user_dict

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0",
                port=8000, reload=True, debug=True)

@app.on_event("startup")
async def on_startup() -> None:
    """
    Event handler for application startup.
    """
    redis = await aioredis.create_redis_pool("redis://localhost")
    await FastAPILimiter.init(redis)

@app.get("/get-courses", dependencies=[Depends(RateLimiter(times=10, seconds=60))])
@cached(ttl=60)
async def get_courses(current_user: User = Depends(get_current_active_user), skip: int = 0, limit: int = 10) -> List[Course]:
    """
    Endpoint to retrieve a list of courses.
    """
    courses = []
    cursor = courses_collection.find({}).skip(skip).limit(limit)
    async for document in cursor:
        courses.append(Course(**document))
    return courses

@app.get("/get-constraints", dependencies=[Depends(RateLimiter(times=10, seconds=60))])
@cached(ttl=60)
async def get_constraints(current_user: User = Depends(get_current_active_user), skip: int = 0, limit: int = 10) -> List[Constraint]:
    """
    Endpoint to retrieve a list of constraints.
    """
    constraints = []
    cursor = constraints_collection.find({}).skip(skip).limit(limit)
    async for document in cursor:
        constraints.append(Constraint(**document))
    return constraints

@app.post("/add-course", response_model=Course)
async def post_course(course: CreateCourse, current_user: User = Depends(get_current_admin_user)) -> Course:
    """
    Endpoint to add a new course.
    """
    document = course.dict()
    await courses_collection.insert_one(document)
    return document

@app.post("/add-constraints", response_model=Constraint)
async def post_constraints(constraint: CreateConstraint, current_user: User = Depends(get_current_admin_user)) -> Constraint:
    """
    Endpoint to add new constraints.
    """
    document = constraint.dict()
    await constraints_collection.insert_one(document)
    return document

@app.get("/generate-timetable")
async def generate_timetable(current_user: User = Depends(get_current_active_user)) -> dict:
    """
    Endpoint to generate a timetable based on constraints and courses.
    """
    constraints = []
    cursor = constraints_collection.find({})
    async for document in cursor:
        constraints.append(Constraint(**document))

    courses = []
    cursor = courses_collection.find({})
    async for document in cursor:
        courses.append(Course(**document))

    if not constraints or not courses:
        logger.error("Constraints or courses are missing")
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
async def update_course(course_id: str, course: UpdateCourse, current_user: User = Depends(get_current_admin_user)) -> Course:
    """
    Endpoint to update an existing course.
    """
    document = course.dict()
    result = await courses_collection.update_one({"_id": course_id}, {"$set": document})
    if result.matched_count == 0:
        logger.error(f"Course with id {course_id} not found")
        raise HTTPException(status_code=404, detail="Course not found")
    updated_course = await courses_collection.find_one({"_id": course_id})
    return updated_course

@app.post("/add-template", response_model=ConstraintTemplate)
async def add_template(template: ConstraintTemplate, current_user: User = Depends(get_current_admin_user)) -> ConstraintTemplate:
    """
    Endpoint to add a new constraint template.
    """
    document = template.dict()
    await templates_collection.insert_one(document)
    return document

@app.get("/get-templates")
async def get_templates(current_user: User = Depends(get_current_active_user)) -> List[ConstraintTemplate]:
    """
    Endpoint to retrieve a list of constraint templates.
    """
    templates = []
    cursor = templates_collection.find({})
    async for document in cursor:
        templates.append(ConstraintTemplate(**document))
    return templates

@app.get("/get-template/{template_id}", response_model=ConstraintTemplate)
async def get_template(template_id: str, current_user: User = Depends(get_current_active_user)) -> ConstraintTemplate:
    """
    Endpoint to retrieve a specific constraint template by ID.
    """
    document = await templates_collection.find_one({"_id": template_id})
    if document is None:
        logger.error(f"Template with id {template_id} not found")
        raise HTTPException(status_code=404, detail="Template not found")
    return ConstraintTemplate(**document)

@app.post("/import-template", response_model=ConstraintTemplate)
async def import_template(template: ConstraintTemplate, current_user: User = Depends(get_current_admin_user)) -> ConstraintTemplate:
    """
    Endpoint to import a constraint template.
    """
    document = template.dict()
    await templates_collection.insert_one(document)
    return document

@app.get("/export-template/{template_id}", response_model=ConstraintTemplate)
async def export_template(template_id: str, current_user: User = Depends(get_current_active_user)) -> ConstraintTemplate:
    """
    Endpoint to export a constraint template by ID.
    """
    document = await templates_collection.find_one({"_id": template_id})
    if document is None:
        logger.error(f"Template with id {template_id} not found")
        raise HTTPException(status_code=404, detail="Template not found")
    return ConstraintTemplate(**document)
