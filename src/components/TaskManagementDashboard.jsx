import React, { useState, useEffect } from "react";
import {
  Typography,
  Container,
  Paper,
  Grid,
  CircularProgress,
  Snackbar,
  Alert,
} from "@mui/material";
import axios from "axios";

const TaskManagementDashboard = () => {
  const [loading, setLoading] = useState(true);
  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTasks = async () => {
      try {
        const trelloResponse = await axios.get("/trello/get-tasks");
        const asanaResponse = await axios.get("/asana/get-tasks");
        setTasks([...trelloResponse.data, ...asanaResponse.data]);
      } catch (error) {
        setError("Failed to fetch tasks");
      } finally {
        setLoading(false);
      }
    };

    fetchTasks();
  }, []);

  return (
    <Container component="main" maxWidth="md" sx={{ mb: 4 }}>
      <Paper variant="outlined" sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 } }}>
        <Typography variant="h6" gutterBottom>
          Task Management Dashboard
        </Typography>
        {loading ? (
          <CircularProgress />
        ) : error ? (
          <Snackbar open={true} autoHideDuration={6000}>
            <Alert severity="error">{error}</Alert>
          </Snackbar>
        ) : (
          <Grid container spacing={3}>
            {tasks.map((task, index) => (
              <Grid item xs={12} key={index}>
                <Paper variant="outlined" sx={{ p: 2 }}>
                  <Typography variant="body1">{task.name}</Typography>
                  <Typography variant="body2">{task.description}</Typography>
                  <Typography variant="body2">
                    Due Date: {task.due_date ? new Date(task.due_date).toLocaleDateString() : "N/A"}
                  </Typography>
                </Paper>
              </Grid>
            ))}
          </Grid>
        )}
      </Paper>
    </Container>
  );
};

export default TaskManagementDashboard;
