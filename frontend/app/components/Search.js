"use client";

import { useSearch } from "../context/SearchContext";
import { useState } from "react";

export default function Search() {
    const { state, submitSearch, resetSearch } = useSearch();
    const [query, setQuery] = useState("");

    // Log state to ensure it's from XState
    console.log("XState current state:", state);

    const handleSearch = () => {
        if (query.trim()) {
            submitSearch(query);
        }
    };

    const handleReset = () => {
        resetSearch();
        setQuery("");
    };

    return (
        <div className="dark flex flex-col items-center">
            <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Enter your query..."
                className="dark border-grey-900 p-2 rounded w-full max-w-md bg-gray-600 text-gray-400"
            />
            <div className="mt-4 flex gap-4">
                <button
                    onClick={handleSearch}
                    className="bg-gray-200 text-black px-4 py-2 rounded hover:bg-gray-300"
                >
                    Search
                </button>
                <button
                    onClick={handleReset}
                    className="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600"
                >
                    Reset
                </button>
            </div>
            {state && state.matches && (
                <p className="mt-4 text-gray-500">
                    Current State: {state.value}
                </p>
            )}
        </div>
    );
}
