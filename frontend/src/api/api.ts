import axios from "axios";

const API = axios.create({
    baseURL: "http://localhost:8000/api",
});

export default API;
