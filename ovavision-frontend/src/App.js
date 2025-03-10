import React, { useState, useEffect } from "react";
import axios from "axios";
import { Loader2, Play, StopCircle, Home, Settings, List } from "lucide-react";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import "./App.css";

const API_URL = "http://127.0.0.1:5000";

// toast.configure();

const Sidebar = ({ setSection }) => (
  <nav className="sidebar">
    <button onClick={() => setSection("status")}><Home /> Status</button>
    <button onClick={() => setSection("controls")}><Settings /> Controls</button>
    <button onClick={() => setSection("logs")}><List /> Logs</button>
  </nav>
);

const Button = ({ children, className, ...props }) => (
  <button className={`btn ${className}`} {...props}>{children}</button>
);

const Card = ({ children, className }) => (
  <div className={`card ${className}`}>{children}</div>
);

const Input = ({ ...props }) => (
  <input className="input" {...props} />
);

const Dashboard = () => {
  const [section, setSection] = useState("status");
  const [status, setStatus] = useState("Stopped");
  const [message, setMessage] = useState("");
  const [x, setX] = useState("");
  const [r, setR] = useState("");
  const [z, setZ] = useState("");
  const [incubator, setIncubator] = useState("");
  const [layer, setLayer] = useState("");
  const [location, setLocation] = useState("");
  const [targetIncubator, setTargetIncubator] = useState("");
  const [targetLayer, setTargetLayer] = useState("");
  const [targetLocation, setTargetLocation] = useState("");
  const [totalEggs, setTotalEggs] = useState(0);
  const [successRate, setSuccessRate] = useState(100);
  const [movementHistory, setMovementHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchStatus();
  }, []);

  const fetchStatus = async () => {
    try {
      const response = await axios.get(`${API_URL}/status`);
      setStatus(response.data.status);
      setMessage(response.data.bin_status);
    } catch (error) {
      console.error("Error fetching status:", error);
    }
  };

  const handleAction = async (action) => {
    try {
      const response = await axios.get(`${API_URL}/${action}`);
      setMessage(response.data.message + "\n" + response.data.bin_status);
      setStatus(response.data.status);
      toast.success(`Machine ${action === "start" ? "started" : "stopped"} successfully`);
    } catch (error) {
      console.error("Error:", error);
      setMessage("Error connecting to server");
      toast.error("Failed to perform action");
    }
  };

  const handleMoveArm = async () => {
    try {
      const response = await axios.post(`${API_URL}/moveArm`, { x, r, z });
      setMessage(response.data.message);
      setStatus(response.data.status);
      toast.success("Arm moved successfully");
    } catch (error) {
      console.error("Error:", error);
      setMessage("Error connecting to server");
      toast.error("Failed to move arm");
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
      setMessage(response.data.message);
      setStatus(response.data.status);
      toast.success("Egg moved successfully");
    } catch (error) {
      console.error("Error:", error);
      setMessage("Error connecting to server");
      toast.error("Failed to move egg");
    }
  };

  return (
    <div className="dashboard-layout">
      <Sidebar setSection={setSection} />
      <main className="dashboard-content">
        {section === "status" && (
          <Card>
            <h1>Status</h1>
            <p><strong>Current Status:</strong> {status}</p>
            <pre>{message}</pre>
            <Button onClick={fetchStatus} className="update-btn"><Loader2 /> Update Status</Button>
          </Card>
        )}
        {section === "controls" && (
          <>
            <Card>
              <h1>Controls</h1>
              <Button onClick={() => handleAction("start")} className="start-btn"><Play /> Start</Button>
              <Button onClick={() => handleAction("stop")} className="stop-btn"><StopCircle /> Stop</Button>
            </Card>
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
          </>
        )}
        {section === "logs" && (
          <>
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
          </>
        )}
      </main>
    </div>
  );
};

export default Dashboard;
