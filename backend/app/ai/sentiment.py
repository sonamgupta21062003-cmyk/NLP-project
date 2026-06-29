"""
Sentiment Analysis Module
"""

import nltk

from nltk.sentiment import SentimentIntensityAnalyzer


# Download only once
try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")


sia = SentimentIntensityAnalyzer()


def predict_sentiment(text: str):

    scores = sia.polarity_scores(text)

    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "Positive"

    elif compound <= -0.05:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "scores": scores
    }