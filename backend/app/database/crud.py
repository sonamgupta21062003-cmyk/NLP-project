from sqlalchemy.orm import Session

from app.database.models import ChatHistory


def save_chat(
    db: Session,
    user_message: str,
    predicted_intent: str,
    sentiment: str,
    confidence: float,
    bot_response: str,
):
    """
    Save one conversation.
    """

    chat = ChatHistory(
        user_message=user_message,
        predicted_intent=predicted_intent,
        sentiment=sentiment,
        confidence=confidence,
        bot_response=bot_response,
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return chat


def get_chat_history(db: Session):
    """
    Return all conversations.
    """

    return db.query(ChatHistory).all()