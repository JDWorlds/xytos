// components/LiveMonitorCard.jsx
import { useEffect, useState } from "react";
import { io } from "socket.io-client";
import LiveChart from "./LiveChart";


export default function LiveMonitorCard() {
  const [data, setData] = useState(null);

  useEffect(() => {

    const socket = io("http://127.0.0.1:5000", {
        transports: ["websocket", "polling"],
        withCredentials: false,
    });

    socket.on("connect", () => {
        console.log("✅ 소켓 연결됨:", socket.id);
    });
  
    socket.on("monitor_data", (payload) => {
        console.log("🟢 데이터 수신:", payload);
        setData(payload);
    });
  
    return () => {
        socket.off("connect");
        socket.off("monitor_data");
    };
  }, []);
  

  return (
    <div className="space-y-6">
      <div className="p-4 bg-white rounded-xl shadow-md">
        <h2 className="text-xl font-bold mb-2">📡 실시간 모니터링</h2>
        {data ? (
          <div className="space-y-1 text-sm">
            <div>설비: {data.equipment_id}</div>
            <div>온도: {data.temperature}°C</div>
            <div>전압: {data.voltage}V</div>
            <div>전류: {data.current}A</div>
            <div>시간: {new Date(data.timestamp).toLocaleTimeString()}</div>
          </div>
        ) : (
          <div>수신 대기 중...</div>
        )}
      </div>
      <LiveChart newData={data} />
    </div>
  );
}