import React, { useState, useEffect } from 'react';
import { getNotifications } from '../api/notifications';
import { motion } from 'framer-motion';

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
          <motion.li
            key={notification.id}
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
          >
            <strong>{notification.title}</strong>: {notification.message}
          </motion.li>
        ))}
      </ul>
    </div>
  );
};

export default NotificationSystem;
