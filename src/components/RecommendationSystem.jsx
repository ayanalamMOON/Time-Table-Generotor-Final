import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { CircularProgress, Typography, Container, Paper, List, ListItem, ListItemText } from '@mui/material';

const RecommendationSystem = () => {
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchRecommendations();
  }, []);

  const fetchRecommendations = async () => {
    try {
      const response = await axios.get('http://localhost:8000/get-recommendations');
      setRecommendations(response.data);
    } catch (error) {
      console.error('Error fetching recommendations:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container component="main" maxWidth="md" sx={{ mb: 4 }}>
      <Paper variant="outlined" sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 } }}>
        <Typography variant="h6" gutterBottom>
          Course Recommendations
        </Typography>
        {loading ? (
          <CircularProgress />
        ) : (
          <List>
            {recommendations.map((recommendation) => (
              <ListItem key={recommendation.id}>
                <ListItemText
                  primary={recommendation.courseName}
                  secondary={recommendation.reason}
                />
              </ListItem>
            ))}
          </List>
        )}
      </Paper>
    </Container>
  );
};

export default RecommendationSystem;
