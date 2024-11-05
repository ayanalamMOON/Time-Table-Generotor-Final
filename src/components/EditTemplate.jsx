import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { TextField, Button, Container, Paper, Typography, CircularProgress, Tooltip } from '@mui/material';
import { useParams } from 'react-router-dom';
import Swal from 'sweetalert2';

const EditTemplate = () => {
  const { id } = useParams();
  const [templateName, setTemplateName] = useState('');
  const [templateDescription, setTemplateDescription] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchTemplate = async () => {
      try {
        const response = await axios.get(`/api/templates/${id}`);
        setTemplateName(response.data.name);
        setTemplateDescription(response.data.description);
      } catch (error) {
        console.error('Error fetching template:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchTemplate();
  }, [id]);

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
      const response = await axios.put(`/api/templates/${id}`, {
        name: templateName,
        description: templateDescription,
      });
      console.log('Template updated:', response.data);
      Swal.fire({
        text: 'Template updated successfully!',
        icon: 'success',
      });
    } catch (error) {
      console.error('Error updating template:', error);
      Swal.fire({
        text: 'Error updating template',
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
          Edit Template
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
            {loading ? <CircularProgress size={24} /> : 'Update Template'}
          </Button>
        </form>
      </Paper>
    </Container>
  );
};

export default EditTemplate;
