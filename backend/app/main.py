"""
Main FastAPI Application Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.db import engine
from app.database.models import Base
from app.api.health import router as health_router
from app.api.routes import router as chat_router

# Generate database tables automatically if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Enterprise AI Customer Support Agent Engine",
    description="Production-grade intent classification, sentiment tracking, and RAG pipeline",
    version="1.0.0"
)

# Apply Cross-Origin Resource Sharing (CORS) configurations 
# This ensures your Streamlit frontend application layer communicates seamlessly.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for locked down production hosting environments later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect individual router submodules cleanly
app.include_router(health_router, tags=["System Health"])
app.include_router(chat_router, prefix="/api/v1", tags=["Core AI Operations"])

@app.get("/")
def root_index():
    """
    Simple verification base index.
    """
    return {
        "application": "AI Customer Support Agent Service Container",
        "documentation_endpoint": "/docs",
        "status": "Operational"
    }