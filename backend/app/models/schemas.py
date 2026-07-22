"""
Pydantic v2 schemas for AI Agent Swarm & Sentiment Engine.
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class SwarmTickInput(BaseModel):
    news_id: str
    headline: str
    impact_weight: float = Field(default=1.0, ge=0.0)

class SwarmTickOutput(SwarmTickInput):
    sentiment_score: float
    simulated_price: float
    buy_orders_count: int
    sell_orders_count: int
    hold_orders_count: int
    net_decision_flow: float

class SwarmSimulationRequest(BaseModel):
    num_agents: int = Field(default=50, ge=5, le=500)
    sentiment_sensitivity: float = Field(default=1.2, ge=0.0)
    impact_multiplier: float = Field(default=0.02, ge=0.0)

class SwarmSimulationResponse(BaseModel):
    total_news_evaluated: int
    overall_sentiment: float
    final_simulated_price: float
    peak_simulated_price: float
    trough_simulated_price: float
    ticks: List[SwarmTickOutput]

class CsvSwarmUploadResponse(BaseModel):
    filename: str
    total_news_parsed: int
    simulation: SwarmSimulationResponse
