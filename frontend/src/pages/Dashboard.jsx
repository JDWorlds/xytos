// pages/Dashboard.jsx
import LiveMonitorCard from "../components/LiveMonitorCard";
import { useEffect, useState } from "react";
import { getSessions } from "../services/api";

export default function Dashboard() {
  const [sessions, setSessions] = useState([]);
  const [latest, setLatest] = useState(null);

  useEffect(() => {
    getSessions().then((res) => setSessions(res.data));
  }, []);

  return (
    <div className="space-y-6">
      <LiveMonitorCard onData={setLatest} />
      <div className="bg-white p-4 rounded-xl shadow">
        <h2 className="text-xl font-semibold mb-2">📄 테스트 세션 목록</h2>
        <table className="table-auto w-full text-sm">
          <thead>
            <tr>
              <th className="text-left">ID</th>
              <th className="text-left">배터리</th>
              <th className="text-left">설비</th>
              <th className="text-left">시작</th>
              <th className="text-left">종료</th>
            </tr>
          </thead>
          <tbody>
            {sessions.map((s) => (
              <tr key={s.id}>
                <td>{s.id}</td>
                <td>{s.battery_id}</td>
                <td>{s.equipment_id}</td>
                <td>{s.start_time}</td>
                <td>{s.end_time || "-"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
