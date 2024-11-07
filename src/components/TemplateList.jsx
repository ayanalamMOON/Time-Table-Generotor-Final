import React, { useState, useEffect, Suspense } from 'react';
import axios from 'axios';
import { TextField, Pagination, Button, Snackbar, Alert, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle } from '@mui/material';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';

const TemplateList = () => {
  const [templates, setTemplates] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const [templatesPerPage] = useState(10);
  const [notification, setNotification] = useState({ open: false, message: '', severity: 'info' });
  const [calendarView, setCalendarView] = useState(false);
  const [openDialog, setOpenDialog] = useState(false);
  const [dialogContent, setDialogContent] = useState({ title: '', content: '', action: null });

  useEffect(() => {
    fetchTemplates();
  }, []);

  const fetchTemplates = async () => {
    try {
      const response = await axios.get('/api/get-templates');
      setTemplates(response.data);
    } catch (error) {
      console.error('Error fetching templates:', error);
    }
  };

  const handleEdit = (templateId) => {
    // Implement edit functionality
  };

  const handleDelete = async (templateId) => {
    try {
      await axios.delete(`/api/templates/${templateId}`);
      fetchTemplates();
      setNotification({ open: true, message: 'Template deleted successfully', severity: 'success' });
    } catch (error) {
      console.error('Error deleting template:', error);
      setNotification({ open: true, message: 'Error deleting template', severity: 'error' });
    }
  };

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
  };

  const filteredTemplates = templates.filter((template) =>
    template.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const indexOfLastTemplate = currentPage * templatesPerPage;
  const indexOfFirstTemplate = indexOfLastTemplate - templatesPerPage;
  const currentTemplates = filteredTemplates.slice(indexOfFirstTemplate, indexOfLastTemplate);

  const paginate = (event, value) => {
    setCurrentPage(value);
  };

  const handleDragEnd = (result) => {
    if (!result.destination) return;
    const reorderedTemplates = Array.from(currentTemplates);
    const [movedTemplate] = reorderedTemplates.splice(result.source.index, 1);
    reorderedTemplates.splice(result.destination.index, 0, movedTemplate);
    setTemplates(reorderedTemplates);
  };

  const toggleCalendarView = () => {
    setCalendarView(!calendarView);
  };

  const handleDialogOpen = (title, content, action) => {
    setDialogContent({ title, content, action });
    setOpenDialog(true);
  };

  const handleDialogClose = () => {
    setOpenDialog(false);
  };

  const handleDialogAction = () => {
    if (dialogContent.action) {
      dialogContent.action();
    }
    handleDialogClose();
  };

  return (
    <div>
      <h2>Template List</h2>
      <TextField
        label="Search Templates"
        variant="outlined"
        value={searchTerm}
        onChange={handleSearch}
        fullWidth
        margin="normal"
      />
      <Button variant="contained" color="primary" onClick={toggleCalendarView}>
        {calendarView ? 'List View' : 'Calendar View'}
      </Button>
      {calendarView ? (
        <Calendar />
      ) : (
        <Suspense fallback={<div>Loading...</div>}>
          <DragDropContext onDragEnd={handleDragEnd}>
            <Droppable droppableId="templates">
              {(provided) => (
                <ul {...provided.droppableProps} ref={provided.innerRef}>
                  {currentTemplates.map((template, index) => (
                    <Draggable key={template.id} draggableId={template.id.toString()} index={index}>
                      {(provided) => (
                        <li ref={provided.innerRef} {...provided.draggableProps} {...provided.dragHandleProps}>
                          {template.name}
                          <button onClick={() => handleEdit(template.id)}>Edit</button>
                          <button onClick={() => handleDialogOpen('Delete Template', 'Are you sure you want to delete this template?', () => handleDelete(template.id))}>Delete</button>
                        </li>
                      )}
                    </Draggable>
                  ))}
                  {provided.placeholder}
                </ul>
              )}
            </Droppable>
          </DragDropContext>
        </Suspense>
      )}
      <Pagination
        count={Math.ceil(filteredTemplates.length / templatesPerPage)}
        page={currentPage}
        onChange={paginate}
        color="primary"
      />
      <Snackbar
        open={notification.open}
        autoHideDuration={6000}
        onClose={() => setNotification({ ...notification, open: false })}
      >
        <Alert onClose={() => setNotification({ ...notification, open: false })} severity={notification.severity}>
          {notification.message}
        </Alert>
      </Snackbar>
      <Dialog
        open={openDialog}
        onClose={handleDialogClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">{dialogContent.title}</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            {dialogContent.content}
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleDialogClose} color="primary">
            Cancel
          </Button>
          <Button onClick={handleDialogAction} color="primary" autoFocus>
            Confirm
          </Button>
        </DialogActions>
      </Dialog>
      <style jsx>{`
        @media (max-width: 600px) {
          h2 {
            font-size: 1.5rem;
          }
          ul {
            padding: 0;
          }
          li {
            font-size: 0.9rem;
          }
        }
      `}</style>
    </div>
  );
};

export default TemplateList;
