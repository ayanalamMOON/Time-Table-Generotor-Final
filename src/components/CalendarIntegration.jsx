import React, { useState } from 'react';
import { Button, Modal, Form } from 'react-bootstrap';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import Swal from 'sweetalert2';

const CalendarIntegration = () => {
  const [showModal, setShowModal] = useState(false);
  const [calendarType, setCalendarType] = useState('');
  const [calendarLink, setCalendarLink] = useState('');

  const handleShowModal = () => setShowModal(true);
  const handleCloseModal = () => setShowModal(false);

  const handleCalendarTypeChange = (e) => setCalendarType(e.target.value);
  const handleCalendarLinkChange = (e) => setCalendarLink(e.target.value);

  const handleSync = () => {
    if (calendarType.trim() === '' || calendarLink.trim() === '') {
      Swal.fire({
        text: 'Please fill in all fields.',
        icon: 'warning',
      });
      return;
    }

    // Add logic to sync schedules with the selected calendar type
    console.log(`Syncing with ${calendarType} using link: ${calendarLink}`);
    handleCloseModal();
  };

  return (
    <div>
      <Button variant="primary" onClick={handleShowModal}>
        Sync with Calendar
      </Button>

      <Modal show={showModal} onHide={handleCloseModal}>
        <Modal.Header closeButton>
          <Modal.Title>Sync with Calendar</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Group controlId="formCalendarType">
              <Form.Label>Calendar Type</Form.Label>
              <Form.Control as="select" value={calendarType} onChange={handleCalendarTypeChange}>
                <option value="">Select Calendar Type</option>
                <option value="google">Google Calendar</option>
                <option value="outlook">Microsoft Outlook</option>
              </Form.Control>
            </Form.Group>
            <Form.Group controlId="formCalendarLink">
              <Form.Label>Calendar Link</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter calendar link"
                value={calendarLink}
                onChange={handleCalendarLinkChange}
              />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleCloseModal}>
            Close
          </Button>
          <Button variant="primary" onClick={handleSync}>
            Sync
          </Button>
        </Modal.Footer>
      </Modal>

      <Calendar />
    </div>
  );
};

export default CalendarIntegration;
