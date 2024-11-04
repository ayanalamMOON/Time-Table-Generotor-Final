import React, { useState } from 'react';
import axios from 'axios';
import { TextField, Button, Container, Paper, Typography } from '@mui/material';

const AddTemplate = () => {
  const [templateName, setTemplateName] = useState('');
  const [templateDescription, setTemplateDescription] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/api/templates', {
        name: templateName,
        description: templateDescription,
      });
      console.log('Template added:', response.data);
      setTemplateName('');
      setTemplateDescription('');
    } catch (error) {
      console.error('Error adding template:', error);
    }
  };

  return (
    <Container component="main" maxWidth="sm">
      <Paper variant="outlined" sx={{ my: 3, p: 3 }}>
        <Typography component="h1" variant="h5">
          Add New Template
        </Typography>
        <form onSubmit={handleSubmit}>
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
          <Button type="submit" fullWidth variant="contained" color="primary">
            Add Template
          </Button>
        </form>
      </Paper>
    </Container>
  );
};

export default AddTemplate;
