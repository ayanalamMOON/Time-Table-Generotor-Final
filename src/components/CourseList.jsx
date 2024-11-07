import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { TextField, Button, Pagination, Snackbar, Alert, Paper, Typography, Tooltip, CircularProgress, MenuItem, Select, FormControl, InputLabel } from '@mui/material';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import { useMediaQuery } from '@mui/material';
import { useTheme } from '@mui/material/styles';

const CourseList = () => {
  const [courses, setCourses] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const [coursesPerPage] = useState(10);
  const [notification, setNotification] = useState({ open: false, message: '', severity: 'success' });
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState('');
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down("sm"));

  useEffect(() => {
    fetchCourses();
  }, []);

  const fetchCourses = async () => {
    try {
      const response = await axios.get('/api/get-courses');
      setCourses(response.data);
    } catch (error) {
      console.error('Error fetching courses:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleEdit = (courseId) => {
    // Implement edit functionality
  };

  const handleDelete = async (courseId) => {
    try {
      await axios.delete(`/api/courses/${courseId}`);
      fetchCourses();
      setNotification({ open: true, message: 'Course deleted successfully', severity: 'success' });
    } catch (error) {
      console.error('Error deleting course:', error);
      setNotification({ open: true, message: 'Error deleting course', severity: 'error' });
    }
  };

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleFilterChange = (event) => {
    setFilter(event.target.value);
  };

  const handleDragEnd = (result) => {
    if (!result.destination) return;

    const reorderedCourses = Array.from(courses);
    const [removed] = reorderedCourses.splice(result.source.index, 1);
    reorderedCourses.splice(result.destination.index, 0, removed);

    setCourses(reorderedCourses);
  };

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase()) &&
    (filter === '' || course.category === filter)
  );

  const indexOfLastCourse = currentPage * coursesPerPage;
  const indexOfFirstCourse = indexOfLastCourse - coursesPerPage;
  const currentCourses = filteredCourses.slice(indexOfFirstCourse, indexOfLastCourse);

  const paginate = (event, value) => {
    setCurrentPage(value);
  };

  const handleCloseNotification = () => {
    setNotification({ ...notification, open: false });
  };

  return (
    <div>
      <h2>Course List</h2>
      {loading ? (
        <CircularProgress />
      ) : (
        <>
          <Tooltip title="Search for courses">
            <TextField
              label="Search Courses"
              variant="outlined"
              value={searchTerm}
              onChange={handleSearch}
              fullWidth
              margin="normal"
            />
          </Tooltip>
          <FormControl fullWidth margin="normal">
            <InputLabel>Filter by Category</InputLabel>
            <Select
              value={filter}
              onChange={handleFilterChange}
              label="Filter by Category"
            >
              <MenuItem value="">All</MenuItem>
              <MenuItem value="Category1">Category1</MenuItem>
              <MenuItem value="Category2">Category2</MenuItem>
              <MenuItem value="Category3">Category3</MenuItem>
            </Select>
          </FormControl>
          <DragDropContext onDragEnd={handleDragEnd}>
            <Droppable droppableId="courses">
              {(provided) => (
                <div {...provided.droppableProps} ref={provided.innerRef}>
                  {currentCourses.map((course, index) => (
                    <Draggable key={course.id} draggableId={course.id.toString()} index={index}>
                      {(provided) => (
                        <div
                          ref={provided.innerRef}
                          {...provided.draggableProps}
                          {...provided.dragHandleProps}
                        >
                          <Paper variant="outlined" sx={{ my: 1, p: 2 }}>
                            <Typography variant="body1">{course.name}</Typography>
                            <button onClick={() => handleEdit(course.id)}>Edit</button>
                            <button onClick={() => handleDelete(course.id)}>Delete</button>
                          </Paper>
                        </div>
                      )}
                    </Draggable>
                  ))}
                  {provided.placeholder}
                </div>
              )}
            </Droppable>
          </DragDropContext>
          <Pagination
            count={Math.ceil(filteredCourses.length / coursesPerPage)}
            page={currentPage}
            onChange={paginate}
            color="primary"
          />
          <Snackbar
            open={notification.open}
            autoHideDuration={6000}
            onClose={handleCloseNotification}
          >
            <Alert onClose={handleCloseNotification} severity={notification.severity}>
              {notification.message}
            </Alert>
          </Snackbar>
        </>
      )}
    </div>
  );
};

export default CourseList;
