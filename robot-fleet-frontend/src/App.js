import React, { useEffect, useState } from 'react';
import { io } from 'socket.io-client';
import MapView from './components/MapView/MapView';
import './App.css'; // Importing CSS for styling

const App = () => {
  const [robotsData, setRobotsData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Connect to WebSocket and listen for real-time updates
  useEffect(() => {
    const socket = io('http://127.0.0.1:5000'); // Flask WebSocket URL

    // Handle connection error
    socket.on('connect_error', (err) => {
      setError('Failed to connect to WebSocket');
      setLoading(false);
    });

    // Listen for updated robot data
    socket.on('robot_data', (data) => {
      setRobotsData(data);
      setLoading(false); // Data received, loading is complete
    });

    // Request to start receiving robot data
    socket.emit('get_robots');

    // Clean up when component is unmounted
    return () => socket.disconnect();
  }, []);

  return (
    <div className="app-container">
      <h1>Robot Fleet Dashboard</h1>

      {/* Show error if connection fails */}
      {error && <div className="error">{error}</div>}

      {/* Robot Details Section */}
      <div className="robot-details">
        {loading ? (
          <p>Loading robots...</p>
        ) : (
          robotsData.length > 0 ? (
            robotsData.map((robot) => (
              <div
                key={robot["Robot ID"]}
                className={`robot-card ${robot["Battery Percentage"] < 20 ? 'low-battery' : ''} ${!robot["Online/Offline"] ? 'offline' : ''}`}
              >
                <h2>{robot["Robot ID"]}</h2>
                <p><strong>Status:</strong> {robot["Online/Offline"] ? 'Online' : 'Offline'}</p>
                <p><strong>Battery:</strong> {robot["Battery Percentage"]}%</p>
                <p><strong>CPU Usage:</strong> {robot["CPU Usage"]}%</p>
                <p><strong>RAM Consumption:</strong> {robot["RAM Consumption"]} MB</p>
                <p><strong>Last Updated:</strong> {robot["Last Updated"]}</p>
              </div>
            ))
          ) : (
            <p>No robots available</p>
          )
        )}
      </div>

      {/* Map View Section */}
      <div className="map-view">
        <MapView robotsData={robotsData} />
      </div>
    </div>
  );
};

export default App;
