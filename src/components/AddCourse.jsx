import React, { useState, useEffect } from "react";
import {
  Typography,
  Stack,
  Paper,
  Grid,
  Container,
  TextField,
  Button,
  CircularProgress,
  Tooltip,
} from "@mui/material";
import { AddCircleOutlined } from "@mui/icons-material";
import Swal from "sweetalert2";
import axios from "axios";

const AddCourse = () => {
  const [courseName, setCourseName] = useState("");
  const [courseCode, setCourseCode] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = () => {
    if (courseName.trim() === "" || courseCode.trim() === "") {
      Swal.fire({
        text: "Please fill in all fields.",
        icon: "warning",
      });
      return;
    }

    const body = {
      name: courseName,
      code: courseCode,
    };
    console.log(body);
    setLoading(true);
    axios
      .post("/api/add-course", body)
      .then(() => {
        Swal.fire({
          text: "Course added successfully!",
          icon: "success",
        });
        setCourseName("");
        setCourseCode("");
      })
      .catch((e) => {
        Swal.fire({
          text: "Error adding course",
          icon: "error",
        });
        console.log(e);
      })
      .finally(() => {
        setLoading(false);
      });
  };

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
                  Add New Course
                </Typography>
              </center>
              <Grid container spacing={3}>
                <Grid item xs={12}>
                  <Tooltip title="Enter the name of the course">
                    <TextField
                      label="Course Name"
                      value={courseName}
                      onChange={(e) => setCourseName(e.target.value)}
                      fullWidth
                    />
                  </Tooltip>
                </Grid>
                <Grid item xs={12}>
                  <Tooltip title="Enter the code of the course">
                    <TextField
                      label="Course Code"
                      value={courseCode}
                      onChange={(e) => setCourseCode(e.target.value)}
                      fullWidth
                    />
                  </Tooltip>
                </Grid>
              </Grid>
              <Stack direction="row" spacing={2} justifyContent="center" sx={{ mt: 3 }}>
                <Button
                  variant="contained"
                  color="primary"
                  startIcon={<AddCircleOutlined />}
                  onClick={handleSubmit}
                >
                  Submit
                </Button>
              </Stack>
            </Paper>
          </Container>
        </>
      )}
    </>
  );
};

export default AddCourse;
