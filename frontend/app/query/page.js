"use client"

import { useSearch } from '../context/SearchContext';
import Search from '../components/Search';

export default function QueryPage() {
    const { results, loading } = useSearch();

    return (
        <div className="min-h-screen bg-gray-100 p-4">
            <header className="py-6 bg-blue-500 text-white text-center">
                <h1 className="text-xl font-bold">AI Search Drift Measuring</h1>
            </header>
            <main className="mt-4">
                <Search />
                {loading && <p className="text-center text-gray-500 mt-4">Loading...</p>}
                <div className="mt-6">
                    {results.map((result, index) => (
                        <div key={index} className="p-4 bg-white shadow rounded mb-4">
                            <p className="font-bold">{result.answer}</p>
                            <p>Similarity: {result.similarity.toFixed(2)}</p>
                            {result.flagged && <p className="text-red-500">Flagged for drift!</p>}
                        </div>
                    ))}
                </div>
            </main>
        </div>
    );
}
