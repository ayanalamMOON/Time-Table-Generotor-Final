import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TemplateList = () => {
  const [templates, setTemplates] = useState([]);

  useEffect(() => {
    fetchTemplates();
  }, []);

  const fetchTemplates = async () => {
    try {
      const response = await axios.get('/api/templates');
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

  return (
    <div>
      <h2>Template List</h2>
      <ul>
        {templates.map((template) => (
          <li key={template.id}>
            {template.name}
            <button onClick={() => handleEdit(template.id)}>Edit</button>
            <button onClick={() => handleDelete(template.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TemplateList;
