from pathlib import Path
from dotenv import load_dotenv
import os

# --------------------------------------------------
# Project Root
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[3]

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv(BASE_DIR / ".env")

# --------------------------------------------------
# Configuration Class
# --------------------------------------------------

class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "distilbert-base-uncased"
    )

    DEBUG = os.getenv(
        "DEBUG",
        "False"
    ).lower() == "true"

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///customer_support.db"
    )


settings = Settings()