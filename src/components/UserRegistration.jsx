import React, { useState } from 'react';
import axios from 'axios';
import { TextField, Button, Container, Paper, Typography, CircularProgress, Tooltip } from '@mui/material';
import Swal from 'sweetalert2';

const UserRegistration = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [fullName, setFullName] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (username.trim() === '' || email.trim() === '' || password.trim() === '' || role.trim() === '') {
      Swal.fire({
        text: 'Please fill in all fields.',
        icon: 'warning',
      });
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post('/api/register', {
        username,
        email,
        full_name: fullName,
        password,
        role,
      });
      console.log('User registered:', response.data);
      setUsername('');
      setEmail('');
      setFullName('');
      setPassword('');
      setRole('');
      Swal.fire({
        text: 'User registered successfully!',
        icon: 'success',
      });
    } catch (error) {
      console.error('Error registering user:', error);
      Swal.fire({
        text: 'Error registering user',
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
          User Registration
        </Typography>
        <form onSubmit={handleSubmit}>
          <Tooltip title="Enter your username">
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="username"
              label="Username"
              name="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </Tooltip>
          <Tooltip title="Enter your email">
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="email"
              label="Email"
              name="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </Tooltip>
          <Tooltip title="Enter your full name">
            <TextField
              variant="outlined"
              margin="normal"
              fullWidth
              id="fullName"
              label="Full Name"
              name="fullName"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
            />
          </Tooltip>
          <Tooltip title="Enter your password">
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="password"
              label="Password"
              name="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </Tooltip>
          <Tooltip title="Enter your role">
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="role"
              label="Role"
              name="role"
              value={role}
              onChange={(e) => setRole(e.target.value)}
            />
          </Tooltip>
          <Button type="submit" fullWidth variant="contained" color="primary">
            Register
          </Button>
        </form>
        {loading && <CircularProgress />}
      </Paper>
    </Container>
  );
};

export default UserRegistration;
