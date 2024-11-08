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
- `UserRegistration.jsx`: A component for user registration.
- `UserLogin.jsx`: A component for user login.
- `RoleBasedAccessControl.jsx`: A component for managing role-based access control.
- `AnalyticsReporting.jsx`: A component for visualizing analytics data and exporting reports.
- `CalendarIntegration.jsx`: A component for integrating and visualizing the timetable in a calendar view.
- `CollaborationFeatures.jsx`: A component for providing real-time collaboration features.

## Technologies Used

The frontend application uses the following technologies:

- React: A JavaScript library for building user interfaces.
- Material-UI: A popular React UI framework for building responsive and customizable components.
- Axios: A promise-based HTTP client for making API requests.
- React Router: A library for handling routing in React applications.
- SweetAlert2: A library for displaying beautiful and customizable alerts.
- React Beautiful DnD: A library for drag-and-drop functionality.
- React Big Calendar: A library for calendar integration and visualization.
- Chart.js: A library for creating charts and graphs.

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

The `Timetable.jsx` component displays the generated timetable. It fetches the timetable data from the backend and renders it in a calendar view. It also provides a drag-and-drop interface for creating and editing timetables.

### `UserRegistration.jsx`

The `UserRegistration.jsx` component provides a form for user registration. It allows users to create a new account by entering their details.

### `UserLogin.jsx`

The `UserLogin.jsx` component provides a form for user login. It allows users to log in to their account by entering their credentials.

### `RoleBasedAccessControl.jsx`

The `RoleBasedAccessControl.jsx` component provides an interface for managing role-based access control. It allows administrators to assign roles and permissions to users.

### `AnalyticsReporting.jsx`

The `AnalyticsReporting.jsx` component provides visualizations for the analytics data, such as charts and graphs. It also allows users to export analytics reports in various formats, such as PDF or Excel.

### `CalendarIntegration.jsx`

The `CalendarIntegration.jsx` component integrates a calendar view to visualize the timetable. It allows users to sync schedules with different calendar types, such as Google Calendar and Microsoft Outlook.

### `CollaborationFeatures.jsx`

The `CollaborationFeatures.jsx` component provides real-time collaboration features, allowing multiple users to work on the same timetable simultaneously. It includes functionalities for adding comments and saving versions.
