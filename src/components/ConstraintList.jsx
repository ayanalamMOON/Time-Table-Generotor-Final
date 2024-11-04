import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ConstraintList = () => {
  const [constraints, setConstraints] = useState([]);

  useEffect(() => {
    fetchConstraints();
  }, []);

  const fetchConstraints = async () => {
    try {
      const response = await axios.get('/api/constraints');
      setConstraints(response.data);
    } catch (error) {
      console.error('Error fetching constraints:', error);
    }
  };

  const handleEdit = (constraintId) => {
    // Implement edit functionality
  };

  const handleDelete = async (constraintId) => {
    try {
      await axios.delete(`/api/constraints/${constraintId}`);
      fetchConstraints();
    } catch (error) {
      console.error('Error deleting constraint:', error);
    }
  };

  return (
    <div>
      <h2>Constraint List</h2>
      <ul>
        {constraints.map((constraint) => (
          <li key={constraint.id}>
            {constraint.name}
            <button onClick={() => handleEdit(constraint.id)}>Edit</button>
            <button onClick={() => handleDelete(constraint.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ConstraintList;
