import joblib
import torch
from pathlib import Path
from app.utils.preprocessing import clean_text

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)


# ==========================================================
# Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

SVM_MODEL_PATH = BASE_DIR / "svm_intent_classifier.pkl"
TFIDF_PATH = BASE_DIR / "tfidf_vectorizer.pkl"
LABEL_ENCODER_PATH = BASE_DIR / "label_encoder.pkl"

BERT_MODEL_PATH = BASE_DIR / "bert_model"


# ==========================================================
# Load Models (Only Once)
# ==========================================================

svm_model = joblib.load(SVM_MODEL_PATH)

tfidf_vectorizer = joblib.load(TFIDF_PATH)

label_encoder = joblib.load(LABEL_ENCODER_PATH)


bert_tokenizer = AutoTokenizer.from_pretrained(BERT_MODEL_PATH)

bert_model = AutoModelForSequenceClassification.from_pretrained(
    BERT_MODEL_PATH
)

bert_model.eval()


# ==========================================================
# SVM Prediction
# ==========================================================

def predict_intent_svm(text: str):

    text = clean_text(text)

    vector = tfidf_vectorizer.transform([text])

    prediction = svm_model.predict(vector)[0]

    intent = label_encoder.inverse_transform([prediction])[0]

    return intent


# ==========================================================
# BERT Prediction
# ==========================================================

def predict_intent_bert(text: str):

    inputs = bert_tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=64
    )

    with torch.no_grad():

        outputs = bert_model(**inputs)

    probabilities = torch.softmax(
        outputs.logits,
        dim=1
    )

    confidence, prediction = torch.max(
        probabilities,
        dim=1
    )

    intent = label_encoder.inverse_transform(
        [prediction.item()]
    )[0]

    return {
        "intent": intent,
        "confidence": float(confidence)
    }
