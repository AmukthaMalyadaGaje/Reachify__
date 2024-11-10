
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import items, auth

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.auth_router)
app.include_router(items.items_router)
