"use client";

import { useSearch } from "../context/SearchContext";
import Search from "../components/Search";

export default function QueryPage() {
    const { state } = useSearch();
    const results = state.context || []; // Safely access results

    console.log("UI: state:", state.value);
    console.log("UI: results:", results.data);

    return (
        <div className="min-h-screen bg-primary p-4">
            <header className="py-6 bg-gray-800 text-white text-center">
                <h1 className="text-xl font-bold">AI Search Drift Measuring</h1>
            </header>
            <main className="bg-primary mt-4">
                <Search />
                {state.value === "searching"&& <p className="text-center text-gray-500 mt-4">Loading...</p>}
                <div className=" mt-6 bg-primary">
                    {state.value==="success" && results.data.length > 0 ? (
                        results.data.map((result, index) => (
                            <div key={index} className="p-4 bg-grey-600shadow rounded mb-4 text-gray-500">
                                <p className="font-bold">{result.answer}</p>
                                <p>Similarity: {result.similarity.toFixed(2)}</p>
                                {result.flagged && (
                                    <p className="text-red-500">Flagged for drift!</p>
                                )}
                            </div>
                        ))
                    ) : (
                        <p className="text-center text-gray-500 mt-4">
                            No results yet. Try a query!
                        </p>
                    )}
                </div>
            </main>
        </div>
    );
}
