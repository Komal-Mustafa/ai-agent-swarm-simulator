"""
Unit tests for AI Swarm Decision Engine, NLP Sentiment Parser, and REST API.
"""

import pytest
import numpy as np
from fastapi.testclient import TestClient

from app.analytics.agent_swarm_engine import simulate_agent_swarm_decisions
from app.analytics.sentiment_parser import calculate_text_sentiment
from app.main import app

client = TestClient(app)

def test_nlp_sentiment_parser():
    pos_headline = "Excellent market growth and profits approved."
    neg_headline = "Unexpected regulatory crash and loss reported."
    
    assert calculate_text_sentiment(pos_headline) > 0.0
    assert calculate_text_sentiment(neg_headline) < 0.0

def test_swarm_decisions():
    sentiments = np.array([0.8, -0.8])
    r = np.array([0.01, 0.01])
    risk = np.array([0.5, 0.5])
    sens = np.array([1.2, 1.2])

    res = simulate_agent_swarm_decisions(sentiments, r, risk, sens, initial_price=100.0)
    assert len(res["prices"]) == 2
    assert len(res["decisions"]) == 2
    # Positive sentiment: agents should buy
    assert np.sum(res["decisions"][0]) > 0
    # Negative sentiment: agents should sell
    assert np.sum(res["decisions"][1]) < 0

def test_api_health():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_api_sample_swarm():
    response = client.get("/api/v1/swarm/sample")
    assert response.status_code == 200
    data = response.json()
    assert data["total_news_evaluated"] == 5
    assert len(data["ticks"]) == 5
