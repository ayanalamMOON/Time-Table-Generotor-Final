# Time Table Generator

This project is a Time Table Generator that allows users to create and manage timetables for various courses and constraints.

## Setup and Run the Project

### Backend

1. Install the required dependencies:

```bash
pip install -r Backend/requirements.txt
```

2. Navigate to the `Backend` directory:

```bash
cd Backend
```

3. Start the backend server:

```bash
uvicorn app:app --reload
```

### Frontend

1. Install the required dependencies:

```bash
npm install
```

2. Start the frontend development server:

```bash
npm start
```

### Docker

1. Build the Docker image:

```bash
docker build -t timetable-generator .
```

2. Run the Docker container:

```bash
docker run -p 8000:8000 timetable-generator
```

### Docker Compose

1. Start the services using Docker Compose:

```bash
docker-compose up
```

## Running the Tests

To run the tests for this project, follow the instructions below:

### Backend Tests

1. Install the required dependencies:

```bash
pip install -r Backend/requirements.txt
```

2. Navigate to the `Backend` directory:

```bash
cd Backend
```

3. Run the tests using `pytest`:

```bash
pytest
```

### Frontend Tests

1. Install the required dependencies:

```bash
npm install
```

2. Run the tests using `Jest`:

```bash
npm test
```

The tests will run and display the results in the terminal.

## Format of Historical Data for AI Model

The historical data for the AI model should be in the following format:

- A list of dictionaries, where each dictionary represents a data point.
- Each dictionary should have two keys: 'features' and 'label'.
  - 'features' should be a list of numerical values representing time series data.
  - 'label' should be a numerical value representing the target variable.

Example:

```python
historical_data = [
    {"features": [0.1, 0.2, 0.3], "label": 1},
    {"features": [0.4, 0.5, 0.6], "label": 0}
]
```

## API Documentation

### Endpoints

#### `GET /get-courses`

Retrieve a list of all courses.

#### `GET /get-constraints`

Retrieve a list of all constraints.

#### `POST /add-course`

Add a new course.

#### `POST /add-constraints`

Add new constraints.

#### `GET /generate-timetable`

Generate a timetable based on the provided constraints and courses.

#### `PUT /update-course/{course_id}`

Update an existing course.

#### `POST /add-template`

Add a new constraint template.

#### `GET /get-templates`

Retrieve a list of all constraint templates.

#### `GET /get-template/{template_id}`

Retrieve a specific constraint template by its ID.

#### `POST /import-template`

Import a constraint template.

#### `GET /export-template/{template_id}`

Export a specific constraint template by its ID.

### Request and Response Examples

#### `POST /add-course`

**Request Body:**

```json
{
  "name": "Test Course",
  "lectureno": 10,
  "duration": 2,
  "instructor_name": "Test Instructor",
  "start_hr": 9,
  "end_hr": 11
}
```

**Response:**

```json
{
  "id": "60c72b2f9b1e8a001c8e4d3b",
  "name": "Test Course",
  "lectureno": 10,
  "duration": 2,
  "instructor_name": "Test Instructor",
  "start_hr": 9,
  "end_hr": 11
}
```

#### `POST /add-constraints`

**Request Body:**

```json
{
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
```

**Response:**

```json
{
  "id": "60c72b2f9b1e8a001c8e4d3c",
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
```

#### `GET /generate-timetable`

**Response:**

```json
{
  "monday": [
    {
      "id": 1,
      "name": "Math",
      "type": "custom",
      "startTime": "2018-02-25T09:00:00",
      "endTime": "2018-02-25T10:00:00"
    }
  ],
  "tuesday": [],
  "wednesday": [],
  "thursday": [],
  "friday": [],
  "saturday": [],
  "sunday": []
}
```
