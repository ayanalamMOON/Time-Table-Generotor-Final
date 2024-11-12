import React, { useState, useEffect } from "react";
import {
  Typography,
  Stack,
  Chip,
  Paper,
  Grid,
  Container,
  TextField,
  Checkbox,
  FormGroup,
  FormControlLabel,
  Autocomplete,
  CircularProgress,
  Button,
  Slider,
  Tooltip,
} from "@mui/material";
import { LocalizationProvider, TimePicker } from "@mui/lab";
import AdapterDateFns from "@mui/lab/AdapterDateFns";
import { AddCircleOutlined } from "@mui/icons-material";
import Swal from "sweetalert2";
import axios from "axios";
import Calendar from "react-calendar";
import "react-calendar/dist/Calendar.css";
import { DragDropContext, Droppable, Draggable } from "react-beautiful-dnd";
import { useMediaQuery } from "@mui/material";
import { useTheme } from "@mui/material/styles";
import { CSSTransition } from "react-transition-group";
import { motion } from "framer-motion";
import "./AddConstraints.css";

const AddConstraints = () => {
  const [selectedDays, setSelectedDays] = useState([]);
  const [timeRange, setTimeRange] = useState([9, 17]);
  const [naturalLanguageTime, setNaturalLanguageTime] = useState("");
  const [checkedA, setCheckedA] = useState(false);
  const [checkedB, setCheckedB] = useState(false);
  const [loading, setLoading] = useState(true);
  const [subjects, setSubjects] = useState([]);
  const [sub1, setSub1] = useState("");
  const [sub2, setSub2] = useState("");
  const [nsub1, setnSub1] = useState("");
  const [nsub2, setnSub2] = useState("");
  const [events, setEvents] = useState([]);
  const [trelloTaskName, setTrelloTaskName] = useState("");
  const [trelloTaskDescription, setTrelloTaskDescription] = useState("");
  const [trelloDueDate, setTrelloDueDate] = useState("");
  const [trelloListId, setTrelloListId] = useState("");
  const [asanaTaskName, setAsanaTaskName] = useState("");
  const [asanaTaskNotes, setAsanaTaskNotes] = useState("");
  const [asanaDueDate, setAsanaDueDate] = useState("");
  const [asanaProjectId, setAsanaProjectId] = useState("");
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down("sm"));

  const handleDayClick = (day) => {
    const newSelectedDays = [...selectedDays];
    const index = newSelectedDays.findIndex(
      (selectedDay) => selectedDay.getTime() === day.getTime()
    );
    if (index > -1) {
      newSelectedDays.splice(index, 1);
    } else {
      newSelectedDays.push(day);
    }
    setSelectedDays(newSelectedDays);
  };

  const handleTimeRangeChange = (event, newValue) => {
    setTimeRange(newValue);
  };

  const handleNaturalLanguageTimeChange = (event) => {
    setNaturalLanguageTime(event.target.value);
  };

  const handleSubmit = () => {
    if (selectedDays.length === 0) {
      Swal.fire({
        text: "Please select at least one day.",
        icon: "warning",
      });
      return;
    }

    if (timeRange[0] >= timeRange[1]) {
      Swal.fire({
        text: "End time must be after start time.",
        icon: "warning",
      });
      return;
    }

    const working_days = selectedDays.map((day) => ({
      day: day.toLocaleDateString("en-US", { weekday: "long" }),
      start_hr: timeRange[0],
      end_hr: timeRange[1],
      total_hours: timeRange[1] - timeRange[0],
    }));

    const consecutive_subjects = [sub1, sub2];
    const non_consecutive_subjects = [nsub1, nsub2];
    const body = {
      working_days: working_days,
      consecutive_subjects: consecutive_subjects,
      non_consecutive_subjects: non_consecutive_subjects,
    };
    console.log(body);
    setLoading(true);
    axios
      .post("/api/add-constraints", body)
      .then(() => {
        Swal.fire({
          text: "Constraints added successfully!",
          icon: "success",
        });
        setSelectedDays([]);
        setTimeRange([9, 17]);
        setNaturalLanguageTime("");
        setCheckedA(false);
        setCheckedB(false);
        setSub1("");
        setSub2("");
        setnSub1("");
        setnSub2("");
      })
      .catch((e) => {
        Swal.fire({
          text: "Error adding constraints",
          icon: "error",
        });
        console.log(e);
      })
      .finally(() => {
        setLoading(false);
      });
  };

  const handleTrelloSubmit = async (event) => {
    event.preventDefault();

    if (trelloTaskName.trim() === '' || trelloTaskDescription.trim() === '' || trelloListId.trim() === '') {
      Swal.fire({
        text: 'Please fill in all fields.',
        icon: 'warning',
      });
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post('/trello/create-task', {
        name: trelloTaskName,
        description: trelloTaskDescription,
        due_date: trelloDueDate,
        list_id: trelloListId,
      });
      console.log('Task created:', response.data);
      setTrelloTaskName('');
      setTrelloTaskDescription('');
      setTrelloDueDate('');
      setTrelloListId('');
      Swal.fire({
        text: 'Task created successfully!',
        icon: 'success',
      });
    } catch (error) {
      console.error('Error creating task:', error);
      Swal.fire({
        text: 'Error creating task',
        icon: 'error',
      });
    } finally {
      setLoading(false);
    }
  };

  const handleAsanaSubmit = async (event) => {
    event.preventDefault();

    if (asanaTaskName.trim() === '' || asanaTaskNotes.trim() === '' || asanaProjectId.trim() === '') {
      Swal.fire({
        text: 'Please fill in all fields.',
        icon: 'warning',
      });
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post('/asana/create-task', {
        name: asanaTaskName,
        notes: asanaTaskNotes,
        due_on: asanaDueDate,
        projects: [asanaProjectId],
      });
      console.log('Task created:', response.data);
      setAsanaTaskName('');
      setAsanaTaskNotes('');
      setAsanaDueDate('');
      setAsanaProjectId('');
      Swal.fire({
        text: 'Task created successfully!',
        icon: 'success',
      });
    } catch (error) {
      console.error('Error creating task:', error);
      Swal.fire({
        text: 'Error creating task',
        icon: 'error',
      });
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    axios.get("http://localhost:8000/get-courses").then((res) => {
      setLoading(false);
      const temp_subjects = [];
      res.data.forEach((item) => {
        temp_subjects.push({ label: item.name, value: item.name });
      });
      setSubjects(temp_subjects);
    });
  }, []);

  const handleDragEnd = (result) => {
    if (!result.destination) return;
    const items = Array.from(events);
    const [reorderedItem] = items.splice(result.source.index, 1);
    items.splice(result.destination.index, 0, reorderedItem);
    setEvents(items);
  };

  return (
    <>
      {loading ? (
        <CircularProgress />
      ) : (
        <>
          <Container component="main" maxWidth="md" sx={{ mb: 4 }}>
            <Paper variant="outlined" sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 } }}>
              <CSSTransition in={!loading} timeout={300} classNames="fade">
                <motion.div
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ duration: 0.5 }}
                >
                  <center>
                    <Typography variant="h6" gutterBottom>
                      Time Table Details
                    </Typography>
                  </center>
                  <Grid container spacing={3}>
                    <Grid item xs={12} sm={3}>
                      <Tooltip title="Select the days for the timetable">
                        <Calendar
                          onClickDay={handleDayClick}
                          tileClassName={({ date }) =>
                            selectedDays.find((selectedDay) => selectedDay.getTime() === date.getTime())
                              ? "selected-day"
                              : ""
                          }
                        />
                      </Tooltip>
                    </Grid>
                    <Grid item xs={12} sm={9}>
                      <Stack direction="row" spacing={1} justifyContent="center">
                        <Tooltip title="Select the time range for the timetable">
                          <Slider
                            value={timeRange}
                            onChange={handleTimeRangeChange}
                            valueLabelDisplay="auto"
                            min={0}
                            max={24}
                            step={1}
                            marks
                          />
                        </Tooltip>
                        <Tooltip title="Enter the time range in natural language">
                          <TextField
                            label="Natural Language Time"
                            value={naturalLanguageTime}
                            onChange={handleNaturalLanguageTimeChange}
                            fullWidth
                          />
                        </Tooltip>
                      </Stack>
                    </Grid>
                  </Grid>
                  <Grid container spacing={3}>
                    <Grid item xs={12} sm={6}>
                      <Tooltip title="Select the first consecutive subject">
                        <Autocomplete
                          options={subjects}
                          getOptionLabel={(option) => option.label}
                          value={sub1}
                          onChange={(event, newValue) => setSub1(newValue)}
                          renderInput={(params) => <TextField {...params} label="Consecutive Subject 1" />}
                        />
                      </Tooltip>
                    </Grid>
                    <Grid item xs={12} sm={6}>
                      <Tooltip title="Select the second consecutive subject">
                        <Autocomplete
                          options={subjects}
                          getOptionLabel={(option) => option.label}
                          value={sub2}
                          onChange={(event, newValue) => setSub2(newValue)}
                          renderInput={(params) => <TextField {...params} label="Consecutive Subject 2" />}
                        />
                      </Tooltip>
                    </Grid>
                    <Grid item xs={12} sm={6}>
                      <Tooltip title="Select the first non-consecutive subject">
                        <Autocomplete
                          options={subjects}
                          getOptionLabel={(option) => option.label}
                          value={nsub1}
                          onChange={(event, newValue) => setnSub1(newValue)}
                          renderInput={(params) => <TextField {...params} label="Non-Consecutive Subject 1" />}
                        />
                      </Tooltip>
                    </Grid>
                    <Grid item xs={12} sm={6}>
                      <Tooltip title="Select the second non-consecutive subject">
                        <Autocomplete
                          options={subjects}
                          getOptionLabel={(option) => option.label}
                          value={nsub2}
                          onChange={(event, newValue) => setnSub2(newValue)}
                          renderInput={(params) => <TextField {...params} label="Non-Consecutive Subject 2" />}
                        />
                      </Tooltip>
                    </Grid>
                  </Grid>
                  <FormGroup>
                    <Tooltip title="Check this option if applicable">
                      <FormControlLabel
                        control={<Checkbox checked={checkedA} onChange={(e) => setCheckedA(e.target.checked)} />}
                        label="Checked A"
                      />
                    </Tooltip>
                    <Tooltip title="Check this option if applicable">
                      <FormControlLabel
                        control={<Checkbox checked={checkedB} onChange={(e) => setCheckedB(e.target.checked)} />}
                        label="Checked B"
                      />
                    </Tooltip>
                  </FormGroup>
                  <DragDropContext onDragEnd={handleDragEnd}>
                    <Droppable droppableId="events">
                      {(provided) => (
                        <div {...provided.droppableProps} ref={provided.innerRef}>
                          {events.map((event, index) => (
                            <Draggable key={event.id} draggableId={event.id} index={index}>
                              {(provided) => (
                                <div
                                  ref={provided.innerRef}
                                  {...provided.draggableProps}
                                  {...provided.dragHandleProps}
                                >
                                  <Paper variant="outlined" sx={{ my: 1, p: 2 }}>
                                    <Typography variant="body1">{event.name}</Typography>
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
                  <Button
                    variant="contained"
                    color="primary"
                    startIcon={<AddCircleOutlined />}
                    onClick={handleSubmit}
                  >
                    Submit
                  </Button>
                  <form onSubmit={handleTrelloSubmit}>
                    <Typography variant="h6" gutterBottom>
                      Trello Task Details
                    </Typography>
                    <Grid container spacing={3}>
                      <Grid item xs={12}>
                        <Tooltip title="Enter the name of the Trello task">
                          <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            id="trelloTaskName"
                            label="Task Name"
                            name="trelloTaskName"
                            value={trelloTaskName}
                            onChange={(e) => setTrelloTaskName(e.target.value)}
                          />
                        </Tooltip>
                      </Grid>
                      <Grid item xs={12}>
                        <Tooltip title="Enter the description of the Trello task">
                          <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            id="trelloTaskDescription"
                            label="Task Description"
                            name="trelloTaskDescription"
                            value={trelloTaskDescription}
                            onChange={(e) => setTrelloTaskDescription(e.target.value)}
                          />
                        </Tooltip>
                      </Grid>
                      <Grid item xs={12}>
                        <Tooltip title="Enter the due date of the Trello task">
                          <TextField
                            variant="outlined"
                            margin="normal"
                            fullWidth
                            id="trelloDueDate"
                            label="Due Date"
                            name="trelloDueDate"
                            type="date"
                            value={trelloDueDate}
                            onChange={(e) => setTrelloDueDate(e.target.value)}
                            InputLabelProps={{
                              shrink: true,
                            }}
                          />
                        </Tooltip>
                      </Grid>
                      <Grid item xs={12}>
                        <Tooltip title="Enter the list ID for the Trello task">
                          <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            id="trelloListId"
                            label="List ID"
                            name="trelloListId"
                            value={trelloListId}
                            onChange={(e) => setTrelloListId(e.target.value)}
                          />
                        </Tooltip>
                      </Grid>
                    </Grid>
                    <Stack direction="row" spacing={2} justifyContent="center" sx={{ mt: 3 }}>
                      <Button type="submit" fullWidth variant="contained" color="primary">
                        {loading ? <CircularProgress size={24} /> : 'Create Task'}
                      </Button>
                    </Stack>
                  </form>
                  <form onSubmit={handleAsanaSubmit}>
                    <Typography variant="h6" gutterBottom>
                      Asana Task Details
                    </Typography>
                    <Grid container spacing={3}>
                      <Grid item xs={12}>
                        <Tooltip title="Enter the name of the Asana task">
                          <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            id="asanaTaskName"
                            label="Task Name"
                            name="asanaTaskName"
                            value={asanaTaskName}
                            onChange={(e) => setAsanaTaskName(e.target.value)}
                          />
                        </Tooltip>
                      </Grid>
                      <Grid item xs={12}>
                        <Tooltip title="Enter the notes for the Asana task">
                          <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            id="asanaTaskNotes"
                            label="Task Notes"
                            name="asanaTaskNotes"
                            value={asanaTaskNotes}
                            onChange={(e) => setAsanaTaskNotes(e.target.value)}
                          />
                        </Tooltip>
                      </Grid>
                      <Grid item xs={12}>
                        <Tooltip title="Enter the due date of the Asana task">
                          <TextField
                            variant="outlined"
                            margin="normal"
                            fullWidth
                            id="asanaDueDate"
                            label="Due Date"
                            name="asanaDueDate"
                            type="date"
                            value={asanaDueDate}
                            onChange={(e) => setAsanaDueDate(e.target.value)}
                            InputLabelProps={{
                              shrink: true,
                            }}
                          />
                        </Tooltip>
                      </Grid>
                      <Grid item xs={12}>
                        <Tooltip title="Enter the project ID for the Asana task">
                          <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            id="asanaProjectId"
                            label="Project ID"
                            name="asanaProjectId"
                            value={asanaProjectId}
                            onChange={(e) => setAsanaProjectId(e.target.value)}
                          />
                        </Tooltip>
                      </Grid>
                    </Grid>
                    <Stack direction="row" spacing={2} justifyContent="center" sx={{ mt: 3 }}>
                      <Button type="submit" fullWidth variant="contained" color="primary">
                        {loading ? <CircularProgress size={24} /> : 'Create Task'}
                      </Button>
                    </Stack>
                  </form>
                </motion.div>
              </CSSTransition>
            </Paper>
          </Container>
        </>
      )}
    </>
  );
};

export default AddConstraints;
