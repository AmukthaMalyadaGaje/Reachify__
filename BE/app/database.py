# app/database.py

from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os

MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client["Reachify"]

# Helper to convert ObjectId to str for JSON response


def item_helper(item):
    return {
        "id": str(item["_id"]),  # Convert ObjectId to string
        "name": item.get("name"),  # Add other fields as needed
        "description": item.get("description"),
        "price": item.get("price"),
        "quantity": item.get("quantity"),
        # Add other fields here based on your item structure
    }
