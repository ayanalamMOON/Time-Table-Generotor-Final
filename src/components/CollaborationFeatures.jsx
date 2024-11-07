import React, { useState, useEffect } from 'react';
import { getCollaborationData, saveCollaborationData } from '../api/collaboration';

const CollaborationFeatures = () => {
  const [collaborationData, setCollaborationData] = useState([]);
  const [newComment, setNewComment] = useState('');

  useEffect(() => {
    fetchCollaborationData();
  }, []);

  const fetchCollaborationData = async () => {
    const data = await getCollaborationData();
    setCollaborationData(data);
  };

  const handleCommentChange = (e) => {
    setNewComment(e.target.value);
  };

  const handleCommentSubmit = async () => {
    const updatedData = await saveCollaborationData(newComment);
    setCollaborationData(updatedData);
    setNewComment('');
  };

  return (
    <div>
      <h2>Collaboration Features</h2>
      <div>
        <h3>Comments</h3>
        <ul>
          {collaborationData.map((item, index) => (
            <li key={index}>{item.comment}</li>
          ))}
        </ul>
        <input
          type="text"
          value={newComment}
          onChange={handleCommentChange}
          placeholder="Add a comment"
        />
        <button onClick={handleCommentSubmit}>Submit</button>
      </div>
    </div>
  );
};

export default CollaborationFeatures;
