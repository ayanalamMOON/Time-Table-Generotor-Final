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

  test('renders calendar view', () => {
    render(<AddConstraints />);
    expect(screen.getByText('Time Table Details')).toBeInTheDocument();
    expect(screen.getByText('Mon')).toBeInTheDocument();
    expect(screen.getByText('Tue')).toBeInTheDocument();
    expect(screen.getByText('Wed')).toBeInTheDocument();
    expect(screen.getByText('Thu')).toBeInTheDocument();
    expect(screen.getByText('Fri')).toBeInTheDocument();
    expect(screen.getByText('Sat')).toBeInTheDocument();
    expect(screen.getByText('Sun')).toBeInTheDocument();
  });

  test('highlights selected days in calendar', () => {
    render(<AddConstraints />);
    const day = screen.getByText('15');
    fireEvent.click(day);
    expect(day).toHaveClass('selected-day');
  });

  test('renders time range slider', () => {
    render(<AddConstraints />);
    expect(screen.getByRole('slider')).toBeInTheDocument();
  });

  test('changes time range slider value', () => {
    render(<AddConstraints />);
    const slider = screen.getByRole('slider');
    fireEvent.change(slider, { target: { value: [10, 18] } });
    expect(slider.value).toBe('10,18');
  });

  test('renders natural language time input', () => {
    render(<AddConstraints />);
    expect(screen.getByLabelText('Natural Language Time')).toBeInTheDocument();
  });

  test('changes natural language time input value', () => {
    render(<AddConstraints />);
    const input = screen.getByLabelText('Natural Language Time');
    fireEvent.change(input, { target: { value: '9 AM to 5 PM' } });
    expect(input.value).toBe('9 AM to 5 PM');
  });
});
