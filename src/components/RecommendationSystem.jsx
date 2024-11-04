import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RecommendationSystem = () => {
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    fetchRecommendations();
  }, []);

  const fetchRecommendations = async () => {
    try {
      const response = await axios.get('/api/recommendations');
      setRecommendations(response.data);
    } catch (error) {
      console.error('Error fetching recommendations:', error);
    }
  };

  return (
    <div>
      <h2>Course Recommendations</h2>
      <ul>
        {recommendations.map((recommendation) => (
          <li key={recommendation.id}>
            {recommendation.courseName} - {recommendation.reason}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RecommendationSystem;
