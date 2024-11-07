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

### `POST /token`

Generate an access token for user authentication.

**Request Body:**

```json
{
  "username": "testuser",
  "password": "testpassword"
}
```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlciIsImV4cCI6MTYyMzQ2OTYwMH0.4f3d5e5f5d6e5f5d6e5f5d6e5f5d6e5f5d6e5f5d6e5f5d6e5f5d6e5f5d6e5f5d6",
  "token_type": "bearer"
}
```

### `POST /register`

Register a new user.

**Request Body:**

```json
{
  "username": "testuser",
  "email": "testuser@example.com",
  "full_name": "Test User",
  "password": "testpassword",
  "role": "user"
}
```

**Response:**

```json
{
  "id": "60c72b2f9b1e8a001c8e4d3e",
  "username": "testuser",
  "email": "testuser@example.com",
  "full_name": "Test User",
  "role": "user"
}
```

### `GET /get-current-user`

Retrieve the current authenticated user.

**Response:**

```json
{
  "id": "60c72b2f9b1e8a001c8e4d3e",
  "username": "testuser",
  "email": "testuser@example.com",
  "full_name": "Test User",
  "role": "user"
}
```

### `GET /get-current-active-user`

Retrieve the current active user.

**Response:**

```json
{
  "id": "60c72b2f9b1e8a001c8e4d3e",
  "username": "testuser",
  "email": "testuser@example.com",
  "full_name": "Test User",
  "role": "user"
}
```

### `GET /get-current-admin-user`

Retrieve the current admin user.

**Response:**

```json
{
  "id": "60c72b2f9b1e8a001c8e4d3e",
  "username": "adminuser",
  "email": "adminuser@example.com",
  "full_name": "Admin User",
  "role": "admin"
}
```

### Error Codes

The following error codes may be returned by the API:

- `400 Bad Request`: The request was invalid or cannot be processed.
- `401 Unauthorized`: Authentication is required and has failed or has not yet been provided.
- `403 Forbidden`: The request was valid, but the server is refusing action. The user might not have the necessary permissions for a resource.
- `404 Not Found`: The requested resource could not be found.
- `500 Internal Server Error`: An error occurred on the server side.

### Usage Scenarios

#### Scenario 1: Registering a new user

1. Send a `POST /register` request with the user's details.
2. Receive a response with the registered user's information.

#### Scenario 2: Logging in and obtaining an access token

1. Send a `POST /token` request with the user's username and password.
2. Receive a response with the access token.

#### Scenario 3: Retrieving a list of courses

1. Send a `GET /get-courses` request with a valid access token.
2. Receive a response with the list of courses.

#### Scenario 4: Adding a new course

1. Send a `POST /add-course` request with the course details and a valid access token.
2. Receive a response with the added course's information.

#### Scenario 5: Generating a timetable

1. Send a `GET /generate-timetable` request with a valid access token.
2. Receive a response with the generated timetable.
