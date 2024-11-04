import React, { useState, useEffect } from 'react';
import axios from 'axios';

const EditConstraints = ({ match, history }) => {
  const [constraint, setConstraint] = useState({
    name: '',
    description: '',
    type: '',
    value: '',
  });

  useEffect(() => {
    const fetchConstraint = async () => {
      try {
        const response = await axios.get(`/api/constraints/${match.params.id}`);
        setConstraint(response.data);
      } catch (error) {
        console.error('Error fetching constraint:', error);
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
    try {
      await axios.put(`/api/constraints/${match.params.id}`, constraint);
      history.push('/constraints');
    } catch (error) {
      console.error('Error updating constraint:', error);
    }
  };

  return (
    <div>
      <h2>Edit Constraint</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={constraint.name}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="description">Description:</label>
          <input
            type="text"
            id="description"
            name="description"
            value={constraint.description}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="type">Type:</label>
          <input
            type="text"
            id="type"
            name="type"
            value={constraint.type}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="value">Value:</label>
          <input
            type="text"
            id="value"
            name="value"
            value={constraint.value}
            onChange={handleChange}
          />
        </div>
        <button type="submit">Save</button>
      </form>
    </div>
  );
};

export default EditConstraints;
