import { createContext, useContext, useState } from 'react';

const ItemContext = createContext();

export const useItemContext = () => useContext(ItemContext);

export const ItemProvider = ({ children }) => {
    const [items, setItems] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    return (
        <ItemContext.Provider value={{ items, setItems, loading, setLoading, error, setError }}>
            {children}
        </ItemContext.Provider>
    );
};
