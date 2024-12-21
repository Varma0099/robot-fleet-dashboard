import React, { useState, useEffect, useRef } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import L from 'leaflet';

function MapView({ robotsData }) {
  const mapRef = useRef(); // Reference for the map container

  // Update the map view whenever the robot positions change
  useEffect(() => {
    if (mapRef.current) {
      mapRef.current.leafletElement.invalidateSize(); // Ensure the map is resized correctly
    }
  }, [robotsData]);

  return (
    <div className="map-container">
      <MapContainer
        center={[51.505, -0.09]} // Default center (can be dynamically updated based on robots' data)
        zoom={13}
        style={{ height: '500px', width: '100%' }}
        whenCreated={(map) => (mapRef.current = map)} // Store the map instance
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />
        {robotsData.map((robot) => (
          <Marker
            key={robot["Robot ID"]}
            position={[robot["Location Coordinates"][0], robot["Location Coordinates"][1]]}
            icon={new L.Icon({ iconUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon.png' })}
          >
            <Popup>
              <strong>Robot ID:</strong> {robot["Robot ID"]} <br />
              <strong>Status:</strong> {robot["Online/Offline"] ? 'Online' : 'Offline'} <br />
              <strong>Battery:</strong> {robot["Battery Percentage"]}% <br />
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
}

export default MapView;
