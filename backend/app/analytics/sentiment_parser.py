"""
Rule-Based Lexicon NLP Sentiment Parsing Engine.
"""

from typing import List, Dict

# Simple financial sentiment keywords lexicon
BULLISH_KEYWORDS = ["surge", "growth", "approved", "bullish", "profit", "gain", "upgrade", "outperform", "acquisition", "strategic"]
BEARISH_KEYWORDS = ["drop", "decline", "rejected", "bearish", "loss", "crash", "downgrade", "deficit", "regulatory", "fine", "investigation"]

def calculate_text_sentiment(text: str) -> float:
    """
    Parses a string headline and scores sentiment on a scale of -1.0 (Bearish) to +1.0 (Bullish).
    """
    clean_text = text.lower()
    bullish_count = sum(1 for w in BULLISH_KEYWORDS if w in clean_text)
    bearish_count = sum(1 for w in BEARISH_KEYWORDS if w in clean_text)
    
    total = bullish_count + bearish_count
    if total == 0:
        return 0.0
    return (bullish_count - bearish_count) / float(total)
