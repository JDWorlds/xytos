import LiveMonitorCard from "./components/LiveMonitorCard";
import { useEffect, useState } from "react";
import { getSessions } from "./services/api";

export default function App() {
  const [sessions, setSessions] = useState([]);

  useEffect(() => {
    getSessions().then((res) => setSessions(res.data));
  }, []);

  return (
    <div className="p-6 space-y-6 bg-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold">🔋 XTOS 배터리 모니터링 대시보드</h1>
      <LiveMonitorCard />
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
