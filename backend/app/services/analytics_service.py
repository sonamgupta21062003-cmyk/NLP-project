"""
Analytics Metrics Processing Service
"""

from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database.models import ChatHistory

def get_platform_analytics(db: Session) -> dict:
    """
    Aggregates metrics tracking total user system interactions.
    """
    total_chats = db.query(ChatHistory).count()
    
    # Calculate average confidence metrics dynamically
    avg_confidence = db.query(func.avg(ChatHistory.confidence)).scalar()
    if avg_confidence is None:
        avg_confidence = 0.0
        
    return {
        "total_chats": total_chats,
        "average_confidence": round(float(avg_confidence), 4)
    }