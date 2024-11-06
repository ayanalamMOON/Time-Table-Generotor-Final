# Frontend Documentation

## Overview

The frontend part of the project is built using React and Material-UI. It provides a user interface for managing courses, constraints, templates, and generating timetables.

## Architecture

The frontend application follows a component-based architecture. Each component is responsible for a specific part of the user interface. The main components are:

- `App.jsx`: The main entry point of the application. It sets up the routing for different pages.
- `AddConstraints.jsx`: A component for adding new constraints.
- `AddCourse.jsx`: A component for adding new courses.
- `AddTemplate.jsx`: A component for adding new templates.
- `ConstraintList.jsx`: A component for displaying a list of constraints.
- `CourseList.jsx`: A component for displaying a list of courses.
- `EditConstraints.jsx`: A component for editing existing constraints.
- `EditCourse.jsx`: A component for editing existing courses.
- `EditTemplate.jsx`: A component for editing existing templates.
- `RecommendationSystem.jsx`: A component for displaying course recommendations.
- `TemplateList.jsx`: A component for displaying a list of templates.
- `Timetable.jsx`: A component for displaying the generated timetable.

## Technologies Used

The frontend application uses the following technologies:

- React: A JavaScript library for building user interfaces.
- Material-UI: A popular React UI framework for building responsive and customizable components.
- Axios: A promise-based HTTP client for making API requests.
- React Router: A library for handling routing in React applications.
- SweetAlert2: A library for displaying beautiful and customizable alerts.

## Setup Instructions

To set up the frontend application, follow these steps:

1. Install the required dependencies:

```bash
npm install
```

2. Start the frontend development server:

```bash
npm start
```

This will start the development server and open the application in your default web browser.

## Component Details

### `App.jsx`

The `App.jsx` file is the main entry point of the application. It sets up the routing for different pages using React Router.

### `AddConstraints.jsx`

The `AddConstraints.jsx` component provides a form for adding new constraints. It allows users to select days, time ranges, and specify consecutive and non-consecutive subjects.

### `AddCourse.jsx`

The `AddCourse.jsx` component provides a form for adding new courses. It allows users to enter the course name and code.

### `AddTemplate.jsx`

The `AddTemplate.jsx` component provides a form for adding new templates. It allows users to enter the template name and description.

### `ConstraintList.jsx`

The `ConstraintList.jsx` component displays a list of constraints. It allows users to search, edit, and delete constraints.

### `CourseList.jsx`

The `CourseList.jsx` component displays a list of courses. It allows users to search, edit, and delete courses.

### `EditConstraints.jsx`

The `EditConstraints.jsx` component provides a form for editing existing constraints. It allows users to update the constraint details.

### `EditCourse.jsx`

The `EditCourse.jsx` component provides a form for editing existing courses. It allows users to update the course details.

### `EditTemplate.jsx`

The `EditTemplate.jsx` component provides a form for editing existing templates. It allows users to update the template details.

### `RecommendationSystem.jsx`

The `RecommendationSystem.jsx` component displays course recommendations. It fetches recommendations from the backend and displays them in a list.

### `TemplateList.jsx`

The `TemplateList.jsx` component displays a list of templates. It allows users to search, edit, and delete templates.

### `Timetable.jsx`

The `Timetable.jsx` component displays the generated timetable. It fetches the timetable data from the backend and renders it in a calendar view.
