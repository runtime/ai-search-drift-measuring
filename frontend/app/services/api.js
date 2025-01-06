import axios from "axios";

export const fetchQueryResults = async (query) => {
    try {
        const response = await axios.post("http://127.0.0.1:8000/query", {
            text: query, // Adjust based on FastAPI's expected payload
        });
        console.log("API Response:", response.data.results);
        return response.data.results; // Assuming API returns results in this format
    } catch (error) {
        console.error("Error fetching query results:", error);
        throw error.response?.data?.detail || "An unknown error occurred";
    }
};

// export async function fetchQueryResults(query) {
//     console.log("API request for query:", query);
//     const response = await fetch(`/api/search?query=${query}`);
//     const data = await response.json();
//     console.log("API response data:", data);
//     return data; // Ensure this returns the expected array or object
// }
