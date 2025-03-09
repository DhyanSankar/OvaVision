import React, { useState, useEffect } from "react";
import axios from "axios";

const API_URL = "http://127.0.0.1:5000"; // Flask backend URL

function App() {
  const [status, setStatus] = useState("Stopped"); // Default status
  const [message, setMessage] = useState(""); // Message from API
  const [x, setX] = useState(""); // X coordinate
  const [r, setR] = useState(""); // R coordinate
  const [z, setZ] = useState(""); // Z coordinate

  useEffect(() => {
    fetchStatus(); // Fetch current status on load
  }, []);

  const fetchStatus = async () => {
    try {
      const response = await axios.get(`${API_URL}/status`);
      setStatus(response.data.status);
      setMessage(response.data.bin_status); // Update message with bin status
    } catch (error) {
      console.error("Error fetching status:", error);
    }
  };

  const handleAction = async (action) => {
    try {
      const response = await axios.get(`${API_URL}/${action}`);
      setMessage(response.data.message + "\n" + response.data.bin_status); // Update message with action message and bin status
      setStatus(response.data.status); // Update status
    } catch (error) {
      console.error("Error:", error);
      setMessage("Error connecting to server");
    }
  };

  const handleMoveArm = async () => {
    try {
      const response = await axios.post(`${API_URL}/moveArm`, { x, r, z });
      setMessage(response.data.message); // Update message
      setStatus(response.data.status); // Update status
    } catch (error) {
      console.error("Error:", error);
      setMessage("Error connecting to server");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Flask-Controlled React App</h1>
      <p><strong>Current Status:</strong> {status}</p>
      <p>{message}</p>
      <button onClick={() => handleAction("start")}>Start</button>
      <button onClick={() => handleAction("stop")}>Stop</button>
      <button onClick={fetchStatus}>Update Status</button>
      <div>
        <h2>Move Arm</h2>
        <input
          type="text"
          placeholder="X coordinate"
          value={x}
          onChange={(e) => setX(e.target.value)}
        />
        <input
          type="text"
          placeholder="R coordinate"
          value={r}
          onChange={(e) => setR(e.target.value)}
        />
        <input
          type="text"
          placeholder="Z coordinate"
          value={z}
          onChange={(e) => setZ(e.target.value)}
        />
        <button onClick={handleMoveArm}>Move Arm</button>
      </div>
    </div>
  );
}

export default App;