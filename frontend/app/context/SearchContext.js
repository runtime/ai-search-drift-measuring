'use client';

import { createContext, useContext } from "react";
import { useMachine } from "@xstate/react";
import { createMachine, assign } from "xstate";
import { fetchQueryResults } from "../services/api";

// Create the Search Context
const SearchContext = createContext();

// Define the Search Machine with an external service
const searchMachine = createMachine({
    id: "search",
    initial: "idle",
    context: {
        results: [], // Results will hold the data fetched from the API
    },
    states: {
        idle: {
            on: { SUBMIT: "searching" }, // Transition to "searching" on SUBMIT
        },
        searching: {
           on: {
                SUCCESS: {
                    target: "success",
                    actions: assign({
                        data: ({ event }) => event.output
                    })
                },
                ERROR: "error",
            },
        },
        success: {
            on: { RESET: "idle" }, // Transition back to "idle" on RESET
        },
        error: {
            on: { RETRY: "searching" }, // Allow retrying the search
        },
    },
});

// Search Context Provider
export const SearchProvider = ({ children }) => {
    const [state, send] = useMachine(searchMachine);

    const submitSearch = async (query) => {
        console.log("Submitting search with query:", query);
        send({ type: "SUBMIT", query }); // Trigger the "SUBMIT" event in the state machine
        const results = await fetchQueryResults(query);
        console.log("Search results from API:", results);
        send({type: "SUCCESS", output: results});
        return results; // Return the API response
    };

    const resetSearch = () => {
        console.log("Resetting search");
        send({ type: "RESET" }); // Trigger the "RESET" event in the state machine
    };

    return (
        <SearchContext.Provider value={{ state, submitSearch, resetSearch }}>
            {children}
        </SearchContext.Provider>
    );
};

// Hook to use the Search Context
export const useSearch = () => {
    return useContext(SearchContext);
};
