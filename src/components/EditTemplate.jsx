import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { TextField, Button, Container, Paper, Typography } from '@mui/material';
import { useParams } from 'react-router-dom';

const EditTemplate = () => {
  const { id } = useParams();
  const [templateName, setTemplateName] = useState('');
  const [templateDescription, setTemplateDescription] = useState('');

  useEffect(() => {
    const fetchTemplate = async () => {
      try {
        const response = await axios.get(`/api/templates/${id}`);
        setTemplateName(response.data.name);
        setTemplateDescription(response.data.description);
      } catch (error) {
        console.error('Error fetching template:', error);
      }
    };

    fetchTemplate();
  }, [id]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.put(`/api/templates/${id}`, {
        name: templateName,
        description: templateDescription,
      });
      console.log('Template updated:', response.data);
    } catch (error) {
      console.error('Error updating template:', error);
    }
  };

  return (
    <Container component="main" maxWidth="sm">
      <Paper variant="outlined" sx={{ my: 3, p: 3 }}>
        <Typography component="h1" variant="h5">
          Edit Template
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
            Update Template
          </Button>
        </form>
      </Paper>
    </Container>
  );
};

export default EditTemplate;
