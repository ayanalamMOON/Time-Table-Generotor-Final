import React, { useState, useEffect } from 'react';
import { getNotifications } from '../api/notifications';

const NotificationSystem = () => {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    const fetchNotifications = async () => {
      const data = await getNotifications();
      setNotifications(data);
    };

    fetchNotifications();
  }, []);

  return (
    <div className="notification-system">
      <h2>Notifications</h2>
      <ul>
        {notifications.map((notification) => (
          <li key={notification.id}>
            <strong>{notification.title}</strong>: {notification.message}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NotificationSystem;
