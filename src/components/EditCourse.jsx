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
} from "@mui/material";
import { EditOutlined } from "@mui/icons-material";
import Swal from "sweetalert2";
import axios from "axios";
import { useParams } from "react-router-dom";

const EditCourse = () => {
  const { courseId } = useParams();
  const [courseName, setCourseName] = useState("");
  const [courseCode, setCourseCode] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchCourseDetails();
  }, []);

  const fetchCourseDetails = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/get-course/${courseId}`);
      setCourseName(response.data.name);
      setCourseCode(response.data.code);
      setLoading(false);
    } catch (error) {
      console.error("Error fetching course details:", error);
      setLoading(false);
    }
  };

  const handleSubmit = () => {
    const body = {
      name: courseName,
      code: courseCode,
    };
    console.log(body);
    setLoading(true);
    axios
      .put(`http://localhost:8000/update-course/${courseId}`, body)
      .then(() => {
        Swal.fire({
          text: "Course updated successfully!",
          icon: "success",
        });
      })
      .catch((e) => {
        Swal.fire({
          text: "Error updating course",
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
                  Edit Course
                </Typography>
              </center>
              <Grid container spacing={3}>
                <Grid item xs={12}>
                  <TextField
                    label="Course Name"
                    value={courseName}
                    onChange={(e) => setCourseName(e.target.value)}
                    fullWidth
                  />
                </Grid>
                <Grid item xs={12}>
                  <TextField
                    label="Course Code"
                    value={courseCode}
                    onChange={(e) => setCourseCode(e.target.value)}
                    fullWidth
                  />
                </Grid>
              </Grid>
              <Stack direction="row" spacing={2} justifyContent="center" sx={{ mt: 3 }}>
                <Button
                  variant="contained"
                  color="primary"
                  startIcon={<EditOutlined />}
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

export default EditCourse;
