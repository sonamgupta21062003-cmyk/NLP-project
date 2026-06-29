# backend/app/api/health.py
from fastapi import APIRouter

# 1. Initialize the router engine cleanly
router = APIRouter()

# 2. Define the path string explicitly as the first argument
@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model": "DistilBERT",
        "version": "1.0.0"
    }