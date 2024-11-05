import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { CircularProgress, TextField, Button, Tooltip } from '@mui/material';
import Swal from 'sweetalert2';

const EditConstraints = ({ match, history }) => {
  const [constraint, setConstraint] = useState({
    name: '',
    description: '',
    type: '',
    value: '',
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchConstraint = async () => {
      try {
        const response = await axios.get(`/api/get-constraint/${match.params.id}`);
        setConstraint(response.data);
      } catch (error) {
        console.error('Error fetching constraint:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchConstraint();
  }, [match.params.id]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setConstraint((prevConstraint) => ({
      ...prevConstraint,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (constraint.name.trim() === '' || constraint.description.trim() === '' || constraint.type.trim() === '' || constraint.value.trim() === '') {
      Swal.fire({
        text: 'Please fill in all fields.',
        icon: 'warning',
      });
      return;
    }

    setLoading(true);
    try {
      await axios.put(`/api/update-constraint/${match.params.id}`, constraint);
      history.push('/constraints');
    } catch (error) {
      console.error('Error updating constraint:', error);
      Swal.fire({
        text: 'Error updating constraint',
        icon: 'error',
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Edit Constraint</h2>
      {loading ? (
        <CircularProgress />
      ) : (
        <form onSubmit={handleSubmit}>
          <div>
            <Tooltip title="Enter the name of the constraint">
              <TextField
                label="Name"
                id="name"
                name="name"
                value={constraint.name}
                onChange={handleChange}
                fullWidth
              />
            </Tooltip>
          </div>
          <div>
            <Tooltip title="Enter the description of the constraint">
              <TextField
                label="Description"
                id="description"
                name="description"
                value={constraint.description}
                onChange={handleChange}
                fullWidth
              />
            </Tooltip>
          </div>
          <div>
            <Tooltip title="Enter the type of the constraint">
              <TextField
                label="Type"
                id="type"
                name="type"
                value={constraint.type}
                onChange={handleChange}
                fullWidth
              />
            </Tooltip>
          </div>
          <div>
            <Tooltip title="Enter the value of the constraint">
              <TextField
                label="Value"
                id="value"
                name="value"
                value={constraint.value}
                onChange={handleChange}
                fullWidth
              />
            </Tooltip>
          </div>
          <Button type="submit" variant="contained" color="primary">
            Save
          </Button>
        </form>
      )}
    </div>
  );
};

export default EditConstraints;
