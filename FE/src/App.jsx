// src/App.js
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { ItemProvider, useItemContext } from "./context/ItemContext";
import Navbar from "./components/Navbar"; // Import Navbar
import Login from "./components/Login";
import Signup from "./components/Signup";
import ItemList from "./components/ItemList";
import PrivateRoute from "./components/PrivateRoute";
import AddItemForm from "./components/AddItemForm";
const App = () => (
  <ItemProvider>
    <Router>
      <Navbar />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route
          path="/items"
          element={
            <PrivateRoute>
              <ItemList />
            </PrivateRoute>
          }
        />
        <Route
          path="/additem"
          element={
            <PrivateRoute>
              <AddItemForm />
            </PrivateRoute>
          }
        />
      </Routes>
    </Router>
  </ItemProvider>
);

export default App;
