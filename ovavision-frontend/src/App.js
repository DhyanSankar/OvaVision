import React, { useState, useEffect } from "react";
import axios from "axios";

const API_URL = "http://127.0.0.1:5000"; // Flask backend URL

function App() {
  const [status, setStatus] = useState("Stopped"); // Default status
  const [message, setMessage] = useState(""); // Message from API

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

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Flask-Controlled React App</h1>
      <p><strong>Current Status:</strong> {status}</p>
      <p>{message}</p>
      <button onClick={() => handleAction("start")}>Start</button>
      <button onClick={() => handleAction("stop")}>Stop</button>
      <button onClick={fetchStatus}>Update Status</button> 
    </div>
  );
}

export default App;
