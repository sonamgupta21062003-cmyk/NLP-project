"""
FastAPI Core Router for Chat Execution
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import process_chat

router = APIRouter()

def get_db():
    """
    Database session dependency generator.
    Ensures safe resource allocation and teardown per request lifecycle.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/chat", response_model=ChatResponse)
def handle_customer_chat(payload: ChatRequest, db: Session = Depends(get_db)):
    """
    Receives incoming customer messages, executes the complete RAG 
    orchestration pipeline, and logs transaction updates to storage.
    """
    try:
        # Pass data cleanly into our tested orchestration service block
        result = process_chat(message=payload.message, db=db)
        
        # Map output to match ChatResponse schema explicitly
        return ChatResponse(
            intent=result["intent"],
            confidence=result["confidence"],
            sentiment=result["sentiment"],
            response=result["response"]
        )
    except Exception as err:
        raise HTTPException(
            status_code=500, 
            detail=f"An error occurred within the orchestration engine: {str(err)}"
        )