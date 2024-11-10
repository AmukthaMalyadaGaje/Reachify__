# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import items, auth

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    # Replace with the origin of your React app
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include routers
app.include_router(auth.auth_router)
app.include_router(items.items_router)
