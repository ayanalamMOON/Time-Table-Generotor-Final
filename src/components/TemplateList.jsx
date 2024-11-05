import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { TextField, Pagination } from '@mui/material';

const TemplateList = () => {
  const [templates, setTemplates] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const [templatesPerPage] = useState(10);

  useEffect(() => {
    fetchTemplates();
  }, []);

  const fetchTemplates = async () => {
    try {
      const response = await axios.get('/api/get-templates');
      setTemplates(response.data);
    } catch (error) {
      console.error('Error fetching templates:', error);
    }
  };

  const handleEdit = (templateId) => {
    // Implement edit functionality
  };

  const handleDelete = async (templateId) => {
    try {
      await axios.delete(`/api/templates/${templateId}`);
      fetchTemplates();
    } catch (error) {
      console.error('Error deleting template:', error);
    }
  };

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
  };

  const filteredTemplates = templates.filter((template) =>
    template.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const indexOfLastTemplate = currentPage * templatesPerPage;
  const indexOfFirstTemplate = indexOfLastTemplate - templatesPerPage;
  const currentTemplates = filteredTemplates.slice(indexOfFirstTemplate, indexOfLastTemplate);

  const paginate = (event, value) => {
    setCurrentPage(value);
  };

  return (
    <div>
      <h2>Template List</h2>
      <TextField
        label="Search Templates"
        variant="outlined"
        value={searchTerm}
        onChange={handleSearch}
        fullWidth
        margin="normal"
      />
      <ul>
        {currentTemplates.map((template) => (
          <li key={template.id}>
            {template.name}
            <button onClick={() => handleEdit(template.id)}>Edit</button>
            <button onClick={() => handleDelete(template.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <Pagination
        count={Math.ceil(filteredTemplates.length / templatesPerPage)}
        page={currentPage}
        onChange={paginate}
        color="primary"
      />
    </div>
  );
};

export default TemplateList;
