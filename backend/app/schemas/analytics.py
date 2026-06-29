from pydantic import BaseModel


class AnalyticsResponse(BaseModel):
    total_chats: int
    average_confidence: float