"""
Text preprocessing utilities.

Every customer message passes through this module
before reaching the intent classifier.
"""

import re


def clean_text(text: str) -> str:
    """
    Basic text cleaning.

    Parameters
    ----------
    text : str
        Customer message.

    Returns
    -------
    str
        Cleaned message.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove leading/trailing spaces
    text = text.strip()

    # Replace multiple spaces with one
    text = re.sub(r"\s+", " ", text)

    # Remove repeated punctuation
    text = re.sub(r"[!?.,]{2,}", " ", text)

    return text