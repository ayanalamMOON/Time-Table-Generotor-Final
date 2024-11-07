import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { TextField, Pagination, CircularProgress, Paper, Typography, Tooltip, MenuItem, Select, InputLabel, FormControl } from '@mui/material';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import { useMediaQuery } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import Swal from 'sweetalert2';

const ConstraintList = () => {
  const [constraints, setConstraints] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const [constraintsPerPage] = useState(10);
  const [loading, setLoading] = useState(true);
  const [events, setEvents] = useState([]);
  const [filterType, setFilterType] = useState('');
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down("sm"));

  useEffect(() => {
    fetchConstraints();
  }, []);

  const fetchConstraints = async () => {
    try {
      const response = await axios.get('/api/get-constraints');
      setConstraints(response.data);
    } catch (error) {
      console.error('Error fetching constraints:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleEdit = (constraintId) => {
    // Implement edit functionality
  };

  const handleDelete = async (constraintId) => {
    try {
      await axios.delete(`/api/constraints/${constraintId}`);
      fetchConstraints();
      Swal.fire({
        text: 'Constraint deleted successfully!',
        icon: 'success',
      });
    } catch (error) {
      console.error('Error deleting constraint:', error);
      Swal.fire({
        text: 'Error deleting constraint',
        icon: 'error',
      });
    }
  };

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleFilterChange = (event) => {
    setFilterType(event.target.value);
  };

  const filteredConstraints = constraints.filter((constraint) =>
    constraint.name.toLowerCase().includes(searchTerm.toLowerCase()) &&
    (filterType === '' || constraint.type === filterType)
  );

  const indexOfLastConstraint = currentPage * constraintsPerPage;
  const indexOfFirstConstraint = indexOfLastConstraint - constraintsPerPage;
  const currentConstraints = filteredConstraints.slice(indexOfFirstConstraint, indexOfLastConstraint);

  const paginate = (event, value) => {
    setCurrentPage(value);
  };

  const handleDragEnd = (result) => {
    if (!result.destination) return;
    const items = Array.from(events);
    const [reorderedItem] = items.splice(result.source.index, 1);
    items.splice(result.destination.index, 0, reorderedItem);
    setEvents(items);
  };

  return (
    <div>
      <h2>Constraint List</h2>
      {loading ? (
        <CircularProgress />
      ) : (
        <>
          <Tooltip title="Search for constraints">
            <TextField
              label="Search Constraints"
              variant="outlined"
              value={searchTerm}
              onChange={handleSearch}
              fullWidth
              margin="normal"
            />
          </Tooltip>
          <FormControl fullWidth margin="normal">
            <InputLabel>Filter by Type</InputLabel>
            <Select
              value={filterType}
              onChange={handleFilterChange}
              label="Filter by Type"
            >
              <MenuItem value="">All</MenuItem>
              <MenuItem value="type1">Type 1</MenuItem>
              <MenuItem value="type2">Type 2</MenuItem>
              <MenuItem value="type3">Type 3</MenuItem>
            </Select>
          </FormControl>
          <DragDropContext onDragEnd={handleDragEnd}>
            <Droppable droppableId="constraints">
              {(provided) => (
                <div {...provided.droppableProps} ref={provided.innerRef}>
                  {currentConstraints.map((constraint, index) => (
                    <Draggable key={constraint.id} draggableId={constraint.id} index={index}>
                      {(provided) => (
                        <div
                          ref={provided.innerRef}
                          {...provided.draggableProps}
                          {...provided.dragHandleProps}
                        >
                          <Paper variant="outlined" sx={{ my: 1, p: 2 }}>
                            <Typography variant="body1">{constraint.name}</Typography>
                            <button onClick={() => handleEdit(constraint.id)}>Edit</button>
                            <button onClick={() => handleDelete(constraint.id)}>Delete</button>
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
            count={Math.ceil(filteredConstraints.length / constraintsPerPage)}
            page={currentPage}
            onChange={paginate}
            color="primary"
          />
        </>
      )}
    </div>
  );
};

export default ConstraintList;
