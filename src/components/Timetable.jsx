import React, { useState, Suspense } from 'react';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import { useMediaQuery } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import Swal from 'sweetalert2';
import { Paper, Typography, Tooltip, Button, Dialog, DialogTitle, DialogContent, DialogActions, TextField } from '@mui/material';
import { motion } from 'framer-motion';

const Timetable = ({ timetable }) => {
  const [events, setEvents] = useState(timetable);
  const [analyticsOpen, setAnalyticsOpen] = useState(false);
  const [collaborationOpen, setCollaborationOpen] = useState(false);
  const [comment, setComment] = useState('');
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down("sm"));

  const handleDragEnd = (result) => {
    if (!result.destination) return;
    const items = Array.from(events);
    const [reorderedItem] = items.splice(result.source.index, 1);
    items.splice(result.destination.index, 0, reorderedItem);
    setEvents(items);
  };

  const handleEventClick = (event) => {
    Swal.fire({
      title: 'Event Details',
      text: `Event: ${event.name}\nTime: ${event.time}`,
      icon: 'info',
    });
  };

  const handleAnalyticsOpen = () => {
    setAnalyticsOpen(true);
  };

  const handleAnalyticsClose = () => {
    setAnalyticsOpen(false);
  };

  const handleCollaborationOpen = () => {
    setCollaborationOpen(true);
  };

  const handleCollaborationClose = () => {
    setCollaborationOpen(false);
  };

  const handleCommentChange = (event) => {
    setComment(event.target.value);
  };

  const handleCommentSubmit = () => {
    // Placeholder for comment submission logic
    console.log('Comment submitted:', comment);
    setComment('');
    setCollaborationOpen(false);
  };

  return (
    <div>
      <Typography variant="h4" gutterBottom>
        Generated Timetable
      </Typography>
      <Calendar />
      <Button variant="contained" color="primary" onClick={handleAnalyticsOpen}>
        View Analytics
      </Button>
      <Button variant="contained" color="secondary" onClick={handleCollaborationOpen}>
        Collaborate
      </Button>
      <Dialog
        open={analyticsOpen}
        onClose={handleAnalyticsClose}
        TransitionComponent={motion.div}
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: 50 }}
        transition={{ duration: 0.5 }}
      >
        <DialogTitle>Analytics and Reporting</DialogTitle>
        <DialogContent>
          {/* Placeholder for analytics and reporting content */}
          <Typography variant="body1">Analytics data goes here...</Typography>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleAnalyticsClose} color="primary">
            Close
          </Button>
        </DialogActions>
      </Dialog>
      <Dialog
        open={collaborationOpen}
        onClose={handleCollaborationClose}
        TransitionComponent={motion.div}
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: 50 }}
        transition={{ duration: 0.5 }}
      >
        <DialogTitle>Collaboration Features</DialogTitle>
        <DialogContent>
          <TextField
            label="Comment"
            value={comment}
            onChange={handleCommentChange}
            fullWidth
            multiline
            rows={4}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCollaborationClose} color="primary">
            Cancel
          </Button>
          <Button onClick={handleCommentSubmit} color="primary">
            Submit
          </Button>
        </DialogActions>
      </Dialog>
      <Suspense fallback={<div>Loading...</div>}>
        <DragDropContext onDragEnd={handleDragEnd}>
          <Droppable droppableId="events">
            {(provided) => (
              <div {...provided.droppableProps} ref={provided.innerRef}>
                <table>
                  <thead>
                    <tr>
                      <th>Time</th>
                      <th>Monday</th>
                      <th>Tuesday</th>
                      <th>Wednesday</th>
                      <th>Thursday</th>
                      <th>Friday</th>
                    </tr>
                  </thead>
                  <tbody>
                    {events.map((row, index) => (
                      <Draggable key={index} draggableId={index.toString()} index={index}>
                        {(provided) => (
                          <tr
                            ref={provided.innerRef}
                            {...provided.draggableProps}
                            {...provided.dragHandleProps}
                            onClick={() => handleEventClick(row)}
                          >
                            <td>{row.time}</td>
                            <td>{row.monday}</td>
                            <td>{row.tuesday}</td>
                            <td>{row.wednesday}</td>
                            <td>{row.thursday}</td>
                            <td>{row.friday}</td>
                          </tr>
                        )}
                      </Draggable>
                    ))}
                  </tbody>
                </table>
                {provided.placeholder}
              </div>
            )}
          </Droppable>
        </DragDropContext>
      </Suspense>
    </div>
  );
};

export default Timetable;
