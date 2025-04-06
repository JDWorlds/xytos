import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import EquipmentView from "./pages/EquipmentView";
import DashExample from "./pages/DashExample";
import "./asset/style.css";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/equipment" element={<EquipmentView />} />
        <Route path="/dashtest" element={<DashExample />} />
      </Routes>
    </Router>
  );
}
