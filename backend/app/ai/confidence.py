"""
Confidence scoring utilities.

This module decides whether the intent prediction
is reliable enough to continue with the AI pipeline.
"""


HIGH_CONFIDENCE = 0.90
MEDIUM_CONFIDENCE = 0.75


def get_confidence_level(score: float) -> str:
    """
    Convert a confidence score into a readable level.
    """

    if score >= HIGH_CONFIDENCE:
        return "HIGH"

    elif score >= MEDIUM_CONFIDENCE:
        return "MEDIUM"

    return "LOW"


def should_escalate(score: float) -> bool:
    """
    Return True if the prediction is too uncertain.
    """

    return score < MEDIUM_CONFIDENCE