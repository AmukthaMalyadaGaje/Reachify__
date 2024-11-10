from pymongo import MongoClient

# Connect to MongoDB (adjust the URL if necessary)
client = MongoClient("mongodb://localhost:27017/")
db = client["Reachify"]  # Replace with your database name
collection = db["items"]  # Replace with your collection name

# Sample data to insert
items = [
    {
        "name": "Apple",
        "description": "Fresh red apple",
        "price": 1.5,
        "quantity": 100
    },
    {
        "name": "Banana",
        "description": "Ripe yellow banana",
        "price": 0.5,
        "quantity": 200
    },
    {
        "name": "Orange",
        "description": "Juicy orange",
        "price": 0.8,
        "quantity": 150
    }
]

# Insert sample data
collection.insert_many(items)

print("Sample data inserted successfully!")
