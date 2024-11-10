import React, { useEffect } from "react";
import { useItemContext } from "../context/ItemContext";
import ItemCard from "./ItemCard";

const ItemList = () => {
  const { items, setItems, loading, setLoading, error, setError } =
    useItemContext();

  useEffect(() => {
    const fetchItems = async () => {
      setLoading(true);
      try {
        const response = await fetch("http://127.0.0.1:8000/items");
        if (!response.ok) throw new Error("Failed to fetch items");
        const data = await response.json();
        setItems(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };
    fetchItems();
  }, [setItems, setLoading, setError]);

  if (loading) return <p className="text-center text-gray-500">Loading...</p>;
  if (error) return <p className="text-center text-red-500">{error}</p>;

  return (
    <div className="max-w-xl mx-auto">
      {items.map((item) => (
        <ItemCard key={item.id} item={item} />
      ))}
    </div>
  );
};

export default ItemList;
