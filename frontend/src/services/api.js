import axios from "axios";

const API = axios.create({
    baseURL: "http://127.0.0.1:5000/api",
});

export const getBatteries = ()=> API.get("/batteries");
export const getEquipment = ()=> API.get("/equipment");
export const getSessions = ()=> API.get("/sessions");
export const createSessions = ()=> API.post("/sessions");
