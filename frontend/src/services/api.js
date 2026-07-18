import axios from "axios";

// Flask Backend URL
const API = axios.create({
    baseURL: "http://127.0.0.1:5000"
});

export default API;