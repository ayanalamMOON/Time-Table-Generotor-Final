# Setup Documentation

This document provides detailed instructions for setting up the Time Table Generator project.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Backend Setup](#backend-setup)
3. [Frontend Setup](#frontend-setup)
4. [Docker Setup](#docker-setup)
5. [Docker Compose Setup](#docker-compose-setup)
6. [Running the Tests](#running-the-tests)
   - [Backend Tests](#backend-tests)
   - [Frontend Tests](#frontend-tests)
7. [Troubleshooting Tips](#troubleshooting-tips)
   - [Common Issues](#common-issues)

## Prerequisites

Before setting up the project, ensure you have the following installed on your system:

- Python 3.9 or higher
- Node.js 14 or higher
- Docker
- Docker Compose

## Backend Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/time-table-generator.git
cd time-table-generator
```

2. Navigate to the `Backend` directory:

```bash
cd Backend
```

3. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the `Backend` directory and add the following environment variables:

```env
MONGODB_CONNECTION_STRING=mongodb://localhost:27017/timetable
```

6. Start the backend server:

```bash
uvicorn app:app --reload
```

## Frontend Setup

1. Navigate to the root directory of the project:

```bash
cd ..
```

2. Install the required dependencies:

```bash
npm install
```

3. Start the frontend development server:

```bash
npm start
```

## Docker Setup

1. Build the Docker image:

```bash
docker build -t timetable-generator .
```

2. Run the Docker container:

```bash
docker run -p 8000:8000 timetable-generator
```

## Docker Compose Setup

1. Start the services using Docker Compose:

```bash
docker-compose up
```

## Running the Tests

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

## Troubleshooting Tips

### Common Issues

1. **Issue**: Backend server not starting.
   **Solution**: Ensure that the MongoDB server is running and the connection string in the `.env` file is correct.

2. **Issue**: Frontend server not starting.
   **Solution**: Ensure that all dependencies are installed correctly by running `npm install` again.

3. **Issue**: Docker container not starting.
   **Solution**: Check the Docker logs for any errors and ensure that the Docker daemon is running.

4. **Issue**: Tests failing.
   **Solution**: Ensure that all dependencies are installed correctly and that the backend server is running before running the tests.
