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
} from "@mui/material";
import { LocalizationProvider, TimePicker } from "@mui/lab";
import AdapterDateFns from "@mui/lab/AdapterDateFns";
import { AddCircleOutlined } from "@mui/icons-material";
import Swal from "sweetalert2";
import axios from "axios";
import Calendar from "react-calendar";
import "react-calendar/dist/Calendar.css";

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
    axios
      .post("http://localhost:8000/add.constraints", body)
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
      .catch((e) => console.log(e));
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

  return (
    <>
      {loading ? (
        <CircularProgress />
      ) : (
        <>
          <Container component="main" maxWidth="md" sx={{ mb: 4 }}>
            <Paper variant="outlined" sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 } }}>
              <center>
                <Typography variant="h6" gutterBottom>
                  Time Table Details
                </Typography>
              </center>
              <Grid container spacing={3}>
                <Grid item xs={12} sm={3}>
                  <Calendar
                    onClickDay={handleDayClick}
                    tileClassName={({ date }) =>
                      selectedDays.find((selectedDay) => selectedDay.getTime() === date.getTime())
                        ? "selected-day"
                        : ""
                    }
                  />
                </Grid>
                <Grid item xs={12} sm={9}>
                  <Stack direction="row" spacing={1} justifyContent="center">
                    <Slider
                      value={timeRange}
                      onChange={handleTimeRangeChange}
                      valueLabelDisplay="auto"
                      min={0}
                      max={24}
                      step={1}
                      marks
                    />
                    <TextField
                      label="Natural Language Time"
                      value={naturalLanguageTime}
                      onChange={handleNaturalLanguageTimeChange}
                      fullWidth
                    />
                  </Stack>
                </Grid>
              </Grid>
              <Grid container spacing={3}>
                <Grid item xs={12} sm={6}>
                  <Autocomplete
                    options={subjects}
                    getOptionLabel={(option) => option.label}
                    value={sub1}
                    onChange={(event, newValue) => setSub1(newValue)}
                    renderInput={(params) => <TextField {...params} label="Consecutive Subject 1" />}
                  />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <Autocomplete
                    options={subjects}
                    getOptionLabel={(option) => option.label}
                    value={sub2}
                    onChange={(event, newValue) => setSub2(newValue)}
                    renderInput={(params) => <TextField {...params} label="Consecutive Subject 2" />}
                  />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <Autocomplete
                    options={subjects}
                    getOptionLabel={(option) => option.label}
                    value={nsub1}
                    onChange={(event, newValue) => setnSub1(newValue)}
                    renderInput={(params) => <TextField {...params} label="Non-Consecutive Subject 1" />}
                  />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <Autocomplete
                    options={subjects}
                    getOptionLabel={(option) => option.label}
                    value={nsub2}
                    onChange={(event, newValue) => setnSub2(newValue)}
                    renderInput={(params) => <TextField {...params} label="Non-Consecutive Subject 2" />}
                  />
                </Grid>
              </Grid>
              <FormGroup>
                <FormControlLabel
                  control={<Checkbox checked={checkedA} onChange={(e) => setCheckedA(e.target.checked)} />}
                  label="Checked A"
                />
                <FormControlLabel
                  control={<Checkbox checked={checkedB} onChange={(e) => setCheckedB(e.target.checked)} />}
                  label="Checked B"
                />
              </FormGroup>
              <Button
                variant="contained"
                color="primary"
                startIcon={<AddCircleOutlined />}
                onClick={handleSubmit}
              >
                Submit
              </Button>
            </Paper>
          </Container>
        </>
      )}
    </>
  );
};

export default AddConstraints;
