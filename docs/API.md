# API Documentation

## Endpoints

### `GET /get-courses`

Retrieve a list of all courses.

**Response:**

```json
[
  {
    "id": "60c72b2f9b1e8a001c8e4d3b",
    "name": "Test Course",
    "lectureno": 10,
    "duration": 2,
    "instructor_name": "Test Instructor",
    "start_hr": 9,
    "end_hr": 11
  }
]
```

### `GET /get-constraints`

Retrieve a list of all constraints.

**Response:**

```json
[
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
]
```

### `POST /add-course`

Add a new course.

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

### `POST /add-constraints`

Add new constraints.

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

### `GET /generate-timetable`

Generate a timetable based on the provided constraints and courses.

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

### `PUT /update-course/{course_id}`

Update an existing course.

**Request Body:**

```json
{
  "name": "Updated Course",
  "lectureno": 15,
  "duration": 3,
  "instructor_name": "Updated Instructor",
  "start_hr": 10,
  "end_hr": 12
}
```

**Response:**

```json
{
  "id": "60c72b2f9b1e8a001c8e4d3b",
  "name": "Updated Course",
  "lectureno": 15,
  "duration": 3,
  "instructor_name": "Updated Instructor",
  "start_hr": 10,
  "end_hr": 12
}
```

### `POST /add-template`

Add a new constraint template.

**Request Body:**

```json
{
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
```

**Response:**

```json
{
  "id": "60c72b2f9b1e8a001c8e4d3d",
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
```

### `GET /get-templates`

Retrieve a list of all constraint templates.

**Response:**

```json
[
  {
    "id": "60c72b2f9b1e8a001c8e4d3d",
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
]
```

### `GET /get-template/{template_id}`

Retrieve a specific constraint template by its ID.

**Response:**

```json
{
  "id": "60c72b2f9b1e8a001c8e4d3d",
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
```

### `POST /import-template`

Import a constraint template.

**Request Body:**

```json
{
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
```

**Response:**

```json
{
  "id": "60c72b2f9b1e8a001c8e4d3d",
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
```

### `GET /export-template/{template_id}`

Export a specific constraint template by its ID.

**Response:**

```json
{
  "id": "60c72b2f9b1e8a001c8e4d3d",
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
```
