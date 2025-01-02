"use client";

import { createContext, useContext, useState } from 'react';

const SearchContext = createContext();

export const useSearch = () => useContext(SearchContext);

export const SearchProvider = ({ children, isClient = false }) => {
    const [results, setResults] = useState([]);
    const [loading, setLoading] = useState(false);

    return (
        <SearchContext.Provider value={{ results, setResults, loading, setLoading, isClient }}>
            {children}
        </SearchContext.Provider>
    );
};
