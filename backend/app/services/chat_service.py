"""
Main Chat Service
"""

from sqlalchemy.orm import Session

from app.ai.intent import predict_intent_bert
from app.ai.sentiment import predict_sentiment

from app.ai.confidence import (
    get_confidence_level,
    should_escalate
)

from app.database.crud import save_chat


def process_chat(
    message: str,
    db: Session
):
    """
    Complete AI pipeline.
    """

    # ------------------------
    # Intent Prediction
    # ------------------------

    intent_result = predict_intent_bert(message)

    intent = intent_result["intent"]

    confidence = intent_result["confidence"]

    # ------------------------
    # Confidence
    # ------------------------

    confidence_level = get_confidence_level(confidence)

    escalation = should_escalate(confidence)

    # ------------------------
    # Sentiment
    # ------------------------

    sentiment_result = predict_sentiment(message)

    sentiment = sentiment_result["sentiment"]

    # ------------------------
    # Temporary Response
    # ------------------------

    response = (
        f"I detected your intent as "
        f"'{intent}'. "
        f"My confidence is "
        f"{confidence:.2f}."
    )

    # ------------------------
    # Save Conversation
    # ------------------------

    save_chat(
        db=db,
        user_message=message,
        predicted_intent=intent,
        sentiment=sentiment,
        confidence=confidence,
        bot_response=response,
    )

    return {

        "intent": intent,

        "confidence": confidence,

        "confidence_level": confidence_level,

        "escalation": escalation,

        "sentiment": sentiment,

        "response": response

    }