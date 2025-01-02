"use client";

import { useState } from "react";

export default function Search() {
    const [query, setQuery] = useState("");

    const handleSearch = async () => {
        console.log("Search query:", query);
        // Add your logic here
        //todo hit the api
    };

    return (
        <div className="flex items-center justify-center h-screen bg-gray-100">
            <div className="w-full max-w-md p-4 bg-white rounded-lg shadow-md">
                <input
                    type="text"
                    placeholder="Enter your query"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    className="w-full px-4 py-2 mb-4 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
                <button
                    onClick={handleSearch}
                    className="w-full px-4 py-2 text-white bg-blue-500 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                    Search
                </button>
            </div>
        </div>
    );
}
