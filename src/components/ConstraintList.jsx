import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { TextField, Pagination } from '@mui/material';

const ConstraintList = () => {
  const [constraints, setConstraints] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const [constraintsPerPage] = useState(10);

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

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
  };

  const filteredConstraints = constraints.filter((constraint) =>
    constraint.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const indexOfLastConstraint = currentPage * constraintsPerPage;
  const indexOfFirstConstraint = indexOfLastConstraint - constraintsPerPage;
  const currentConstraints = filteredConstraints.slice(indexOfFirstConstraint, indexOfLastConstraint);

  const paginate = (event, value) => {
    setCurrentPage(value);
  };

  return (
    <div>
      <h2>Constraint List</h2>
      <TextField
        label="Search Constraints"
        variant="outlined"
        value={searchTerm}
        onChange={handleSearch}
        fullWidth
        margin="normal"
      />
      <ul>
        {currentConstraints.map((constraint) => (
          <li key={constraint.id}>
            {constraint.name}
            <button onClick={() => handleEdit(constraint.id)}>Edit</button>
            <button onClick={() => handleDelete(constraint.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <Pagination
        count={Math.ceil(filteredConstraints.length / constraintsPerPage)}
        page={currentPage}
        onChange={paginate}
        color="primary"
      />
    </div>
  );
};

export default ConstraintList;
