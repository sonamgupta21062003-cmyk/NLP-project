"""
Security and validation utility layers for the NLP Preprocessing Pipeline.
"""
import re

def sanitize_input_text(text: str) -> str:
    """
    Strips raw HTML markup elements from incoming user payloads 
    to preserve pure text tokens for downstream NLP model inference.
    """
    if not text:
        return ""
    
    # Remove leading and trailing whitespace characters
    cleaned = text.strip()
    
    # Strip HTML/XML tag structures completely so they do not pollute token patterns
    cleaned = re.sub(r'<[^>]*>', '', cleaned)
    
    return cleaned