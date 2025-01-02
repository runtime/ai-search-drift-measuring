import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000';

export const fetchQueryResults = async (query) => {
    try {
        const response = await axios.post(`${API_URL}/query`, { text: query });
        return response.data.results;
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
};
