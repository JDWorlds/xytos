import { useEffect, useState } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Legend,
} from "recharts";

export default function LiveChart({ newData }) {
  const [data, setData] = useState([]);
  const [fixedYAxis, setFixedYAxis] = useState(false); // Y축 고정 여부

  useEffect(() => {
    if (!newData) return;
    setData((prev) => {
      const updated = [...prev, newData];
      return updated.slice(-20); // 최근 20개 유지
    });
  }, [newData]);

  // Y축 도메인 설정
  const yDomain = fixedYAxis ? [0, 100] : ["auto", "auto"];

  return (
    <div className="bg-white p-4 rounded-xl shadow-md">
      <div className="flex justify-between items-center mb-2">
        <h2 className="text-lg font-bold">📊 실시간 배터리 그래프</h2>
        <button
          className="text-sm px-2 py-1 border rounded hover:bg-gray-100"
          onClick={() => setFixedYAxis(!fixedYAxis)}
        >
          Y축: {fixedYAxis ? "고정" : "자동"}
        </button>
      </div>

      <LineChart width={600} height={250} data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis
          dataKey="timestamp"
          tickFormatter={(time) => new Date(time).toLocaleTimeString()}
        />
        <YAxis domain={yDomain} />
        <Tooltip labelFormatter={(time) => new Date(time).toLocaleTimeString()} />
        <Legend />
        <Line
          type="monotone"
          dataKey="temperature"
          stroke="#ff7300"
          name="온도 (°C)"
        />
        <Line
          type="monotone"
          dataKey="voltage"
          stroke="#387908"
          name="전압 (V)"
        />
        <Line
          type="monotone"
          dataKey="current"
          stroke="#007bff"
          name="전류 (A)"
        />
      </LineChart>
    </div>
  );
}