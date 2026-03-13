import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface AttendanceData {
  date: string;
  total_present: number;
  total_absent: number;
  attendance_percentage: number;
}

function App() {
  const [apiStatus, setApiStatus] = useState<string>('Checking...');
  const [attendance, setAttendance] = useState<AttendanceData | null>(null);

  useEffect(() => {
    // Check backend connection
    axios.get('http://localhost:8000/health')
      .then(res => setApiStatus('Connected ✅'))
      .catch(err => setApiStatus('Disconnected ❌'));

    // Get attendance data
    axios.get('http://localhost:8000/api/v1/attendance/today')
      .then(res => setAttendance(res.data))
      .catch(err => console.log('Error fetching attendance:', err));
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>🎓 Smart Attendance System</h1>
      <p>Backend Status: <strong>{apiStatus}</strong></p>
      
      {attendance ? (
        <div style={{ 
          backgroundColor: '#f5f5f5', 
          padding: '20px', 
          borderRadius: '8px',
          marginTop: '20px'
        }}>
          <h2>Today's Attendance</h2>
          <p><strong>Date:</strong> {attendance.date}</p>
          <p><strong>Present:</strong> {attendance.total_present}</p>
          <p><strong>Absent:</strong> {attendance.total_absent}</p>
          <p><strong>Percentage:</strong> {attendance.attendance_percentage}%</p>
        </div>
      ) : (
        <p>Loading attendance data...</p>
      )}
    </div>
  );
}

export default App;