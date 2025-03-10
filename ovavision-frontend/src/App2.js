import React, { useState, useEffect } from "react";
import axios from "axios";
import { Loader2, Play, StopCircle, Sun, Moon } from "lucide-react";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import "./App.css";

const API_URL = "http://127.0.0.1:5000"; // Flask backend URL

const Button = ({ children, className, ...props }) => (
  <button className={`btn ${className}`} {...props}>{children}</button>
);

const Card = ({ children, className }) => (
  <div className={`card ${className}`}>{children}</div>
);

const Input = ({ ...props }) => (
  <input className="input" {...props} />
);

function App() {
  const [status, setStatus] = useState("Stopped"); // Default status
  const [message, setMessage] = useState(""); // Message from API
  const [x, setX] = useState(""); // X coordinate
  const [r, setR] = useState(""); // R coordinate
  const [z, setZ] = useState(""); // Z coordinate
  const [incubator, setIncubator] = useState(""); // Incubator number
  const [layer, setLayer] = useState(""); // Layer number
  const [location, setLocation] = useState(""); // Location number
  const [targetIncubator, setTargetIncubator] = useState(""); // Target incubator number
  const [targetLayer, setTargetLayer] = useState(""); // Target layer number
  const [targetLocation, setTargetLocation] = useState(""); // Target location number

  const [totalEggs, setTotalEggs] = useState(0);
  const [successRate, setSuccessRate] = useState(100);
  const [movementHistory, setMovementHistory] = useState([]);
  const [loading, setLoading] = useState(false);

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

  const handleMoveEgg = async () => {
    try {
      const response = await axios.post(`${API_URL}/moveEgg`, {
        incubator,
        layer,
        location,
        target_incubator: targetIncubator,
        target_layer: targetLayer,
        target_location: targetLocation,
      });
      setMessage(response.data.message); // Update message
      setStatus(response.data.status); // Update status
    } catch (error) {
      console.error("Error:", error);
      setMessage("Error connecting to server");
    }
  };

  return (
    <div className={`container`}>

      <Card className="text-center">
        <h1>Egg Incubator Controller</h1>
        <p><strong>Current Status:</strong> {status}</p>
        <p>{message}</p>
        <div className="button-group">
          <Button onClick={() => handleAction("start")} className="start-btn">
            {loading ? <Loader2 className="spinner" /> : <Play />} Start
          </Button>
          <Button onClick={() => handleAction("stop")} className="stop-btn">
            {loading ? <Loader2 className="spinner" /> : <StopCircle />} Stop
          </Button>
          <Button onClick={fetchStatus} className="update-btn"><Loader2 /> Update Status</Button>
        </div>
      </Card>

      <div className="grid">
        <Card>
          <h2>Move Arm</h2>
          <div className="input-group">
            <Input placeholder="X coordinate" value={x} onChange={(e) => setX(e.target.value)} />
            <Input placeholder="R coordinate" value={r} onChange={(e) => setR(e.target.value)} />
            <Input placeholder="Z coordinate" value={z} onChange={(e) => setZ(e.target.value)} />
            <Button onClick={handleMoveArm} className="move-btn">Move Arm</Button>
          </div>
        </Card>

        <Card>
          <h2>Move Egg</h2>
          <div className="input-group">
            <Input placeholder="Incubator #" value={incubator} onChange={(e) => setIncubator(e.target.value)} />
            <Input placeholder="Layer #" value={layer} onChange={(e) => setLayer(e.target.value)} />
            <Input placeholder="Location #" value={location} onChange={(e) => setLocation(e.target.value)} />
            <Input placeholder="Target Incubator #" value={targetIncubator} onChange={(e) => setTargetIncubator(e.target.value)} />
            <Input placeholder="Target Layer #" value={targetLayer} onChange={(e) => setTargetLayer(e.target.value)} />
            <Input placeholder="Target Location #" value={targetLocation} onChange={(e) => setTargetLocation(e.target.value)} />
            <Button onClick={handleMoveEgg} className="move-btn">Move Egg</Button>
          </div>
        </Card>

        <Card>
          <h2>Egg Sorting Stats</h2>
          <p>Total Eggs Sorted: {totalEggs}</p>
          <p>Success Rate: {successRate.toFixed(2)}%</p>
        </Card>

        <Card>
          <h2>Egg Movement History</h2>
          <ul>
            {movementHistory.map((item, index) => (
              <li key={index}>Egg moved from {item.from} to {item.to} at {item.time}</li>
            ))}
          </ul>
        </Card>
      </div>
    </div>
  );
}

export default App;
