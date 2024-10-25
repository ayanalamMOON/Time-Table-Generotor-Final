import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import AddConstraints from '../components/AddConstraints';
import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';
import Swal from 'sweetalert2';

const mock = new MockAdapter(axios);

describe('AddConstraints Component', () => {
  beforeEach(() => {
    mock.reset();
  });

  test('renders AddConstraints component', () => {
    render(<AddConstraints />);
    expect(screen.getByText('Time Table Details')).toBeInTheDocument();
  });

  test('adds constraints successfully', async () => {
    mock.onPost('http://localhost:8000/add.constraints').reply(200);

    render(<AddConstraints />);

    fireEvent.click(screen.getByText('Monday'));
    fireEvent.click(screen.getByText('Tuesday'));

    fireEvent.change(screen.getByLabelText('Start Time'), { target: { value: '09:00' } });
    fireEvent.change(screen.getByLabelText('End Time'), { target: { value: '17:00' } });

    fireEvent.click(screen.getByText('Submit'));

    await screen.findByText('Constraints added successfully!');

    expect(Swal.fire).toHaveBeenCalledWith({
      text: 'Constraints added successfully!',
      icon: 'success',
    });
  });

  test('handles API error', async () => {
    mock.onPost('http://localhost:8000/add.constraints').reply(500);

    render(<AddConstraints />);

    fireEvent.click(screen.getByText('Monday'));
    fireEvent.click(screen.getByText('Tuesday'));

    fireEvent.change(screen.getByLabelText('Start Time'), { target: { value: '09:00' } });
    fireEvent.change(screen.getByLabelText('End Time'), { target: { value: '17:00' } });

    fireEvent.click(screen.getByText('Submit'));

    await screen.findByText('Error adding constraints');

    expect(Swal.fire).toHaveBeenCalledWith({
      text: 'Error adding constraints',
      icon: 'error',
    });
  });
});
