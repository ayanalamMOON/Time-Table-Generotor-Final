import React, { useState } from 'react';
import axios from 'axios';
import { TextField, Button, Container, Paper, Typography, CircularProgress, Tooltip } from '@mui/material';
import Swal from 'sweetalert2';

const AddTemplate = () => {
  const [templateName, setTemplateName] = useState('');
  const [templateDescription, setTemplateDescription] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (templateName.trim() === '' || templateDescription.trim() === '') {
      Swal.fire({
        text: 'Please fill in all fields.',
        icon: 'warning',
      });
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post('/api/templates', {
        name: templateName,
        description: templateDescription,
      });
      console.log('Template added:', response.data);
      setTemplateName('');
      setTemplateDescription('');
      Swal.fire({
        text: 'Template added successfully!',
        icon: 'success',
      });
    } catch (error) {
      console.error('Error adding template:', error);
      Swal.fire({
        text: 'Error adding template',
        icon: 'error',
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container component="main" maxWidth="sm">
      <Paper variant="outlined" sx={{ my: 3, p: 3 }}>
        <Typography component="h1" variant="h5">
          Add New Template
        </Typography>
        <form onSubmit={handleSubmit}>
          <Tooltip title="Enter the name of the template">
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="templateName"
              label="Template Name"
              name="templateName"
              value={templateName}
              onChange={(e) => setTemplateName(e.target.value)}
            />
          </Tooltip>
          <Tooltip title="Enter the description of the template">
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="templateDescription"
              label="Template Description"
              name="templateDescription"
              value={templateDescription}
              onChange={(e) => setTemplateDescription(e.target.value)}
            />
          </Tooltip>
          <Button type="submit" fullWidth variant="contained" color="primary">
            Add Template
          </Button>
        </form>
        {loading && <CircularProgress />}
      </Paper>
    </Container>
  );
};

export default AddTemplate;
