"""
Database Models
"""

from sqlalchemy import Column , Integer,String,Float,Text,DateTime
from datetime import datetime

from app.database.db import Base

class ChatHistory(Base):
    __tablename__ ="chat_history"

    id = Column(Integer,primary_key=True,index=True)

    user_message = Column(Text,nullable=False)

    predicted_intent = Column(String,nullable = False)

    sentiment = Column(String,nullable=False)

    confidence = Column(Float,nullable=False)

    bot_response = Column(Text,nullable=False)

    created_at = Column(DateTime,default = datetime.utcnow)

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)

    message_id = Column(Integer)

    rating = Column(Integer)

    comments = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)


class Analytics(Base):
    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True, index=True)

    intent = Column(String)

    sentiment = Column(String)

    confidence = Column(Float)

    created_at = Column(DateTime, default=datetime.utcnow)   