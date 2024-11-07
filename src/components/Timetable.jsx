import React, { useState } from 'react';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import { useMediaQuery } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import Swal from 'sweetalert2';
import { Paper, Typography, Tooltip } from '@mui/material';

const Timetable = ({ timetable }) => {
  const [events, setEvents] = useState(timetable);
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

  return (
    <div>
      <Typography variant="h4" gutterBottom>
        Generated Timetable
      </Typography>
      <Calendar />
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
    </div>
  );
};

export default Timetable;
