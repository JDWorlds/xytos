import { useEffect } from "react";

export default function EquipmentView() {
  useEffect(() => {
    const script = document.createElement("script");
    script.src = "/dash_example.js"; // public/script.js 위치
    script.type = "module";
    script.async = true;
    script.onload = () => {
      console.log("Dashboard script loaded");
      };
    
      document.body.appendChild(script);

    return () => {
      document.body.removeChild(script); // cleanup
    };
  }, []);

  return <div id="my-dashboard">장비 상태</div>;
}
