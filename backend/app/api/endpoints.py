"""
FastAPI REST Endpoints for Multi-Agent AI Financial Swarm Simulation.
"""

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import pandas as pd
import numpy as np
import io
from typing import Optional, List, Dict, Any

from app.models.schemas import (
    SwarmTickInput,
    SwarmTickOutput,
    SwarmSimulationRequest,
    SwarmSimulationResponse,
    CsvSwarmUploadResponse
)
from app.analytics.agent_swarm_engine import simulate_agent_swarm_decisions
from app.analytics.sentiment_parser import calculate_text_sentiment
from app.data.sample_news import SAMPLE_NEWS

router = APIRouter(prefix="/api/v1", tags=["AI Swarm API"])


@router.get("/health")
def health():
    return {"status": "healthy", "service": "AI Swarm Simulation API", "version": "1.0.0"}


@router.get("/swarm/sample", response_model=SwarmSimulationResponse)
def get_sample_swarm_simulation(
    num_agents: int = 50,
    sentiment_sensitivity: float = 1.2,
    impact_multiplier: float = 0.02
):
    """Fetches sample Bloomberg financial news and simulates AI Agent Swarm order book updates."""
    news = [SwarmTickInput(**n) for n in SAMPLE_NEWS]
    req = SwarmSimulationRequest(
        num_agents=num_agents,
        sentiment_sensitivity=sentiment_sensitivity,
        impact_multiplier=impact_multiplier
    )
    return _run_swarm_simulation(news, req)


@router.post("/swarm/upload-csv", response_model=CsvSwarmUploadResponse)
async def upload_swarm_csv(
    file: UploadFile = File(...),
    num_agents: int = Form(50),
    sentiment_sensitivity: float = Form(1.2),
    impact_multiplier: float = Form(0.02)
):
    """Ingests custom news feed CSV and simulates AI Agent Swarm price updates."""
    if not file.filename.endswith(('.csv', '.txt')):
        raise HTTPException(status_code=400, detail="Only .csv and text files are supported.")

    content = await file.read()
    try:
        df = pd.read_csv(io.BytesIO(content))
    except Exception:
        try:
            df = pd.read_csv(io.BytesIO(content), sep=None, engine='python')
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Failed to parse CSV file: {str(e)}")

    if df.empty:
        raise HTTPException(status_code=400, detail="Uploaded CSV file is empty.")

    cols_lower = {col.lower().strip().replace(" ", "_"): col for col in df.columns}

    id_col = cols_lower.get('news_id', cols_lower.get('id', df.columns[0]))
    headline_col = cols_lower.get('headline', cols_lower.get('text', cols_lower.get('title', df.columns[0])))
    weight_col = cols_lower.get('impact_weight', cols_lower.get('weight', df.columns[0]))

    def _safe_float(val, default_val: float) -> float:
        try:
            n = float(pd.to_numeric(val, errors='coerce'))
            return default_val if np.isnan(n) else n
        except Exception:
            return default_val

    news: List[SwarmTickInput] = []
    for idx, row in df.iterrows():
        try:
            news.append(SwarmTickInput(
                news_id=str(row.get(id_col, f"NEWS-{idx+1}")),
                headline=str(row.get(headline_col, f"Headline {idx+1}")),
                impact_weight=_safe_float(row.get(weight_col), 1.0)
            ))
        except Exception:
            continue

    if not news:
        raise HTTPException(status_code=400, detail="No valid news headlines could be parsed from the CSV.")

    req = SwarmSimulationRequest(
        num_agents=num_agents,
        sentiment_sensitivity=sentiment_sensitivity,
        impact_multiplier=impact_multiplier
    )

    simulation = _run_swarm_simulation(news, req)
    return CsvSwarmUploadResponse(
        filename=file.filename,
        total_news_parsed=len(news),
        simulation=simulation
    )


def _run_swarm_simulation(news: List[SwarmTickInput], req: SwarmSimulationRequest) -> SwarmSimulationResponse:
    sentiments = np.array([calculate_text_sentiment(n.headline) * n.impact_weight for n in news])
    
    # Initialize agent parameters
    np.random.seed(42)
    baseline_r = np.random.uniform(-0.01, 0.02, req.num_agents)
    risk_aversion = np.random.uniform(0.1, 1.5, req.num_agents)
    sensitivities = np.random.uniform(0.5, 2.0, req.num_agents) * req.sentiment_sensitivity

    sim = simulate_agent_swarm_decisions(
        sentiments, baseline_r, risk_aversion, sensitivities,
        initial_price=100.0, impact_multiplier=req.impact_multiplier
    )

    outputs: List[SwarmTickOutput] = []
    prices = sim["prices"]
    decisions = sim["decisions"]

    for i, n in enumerate(news):
        act = decisions[i]
        buys = int(np.sum(act == 1.0))
        sells = int(np.sum(act == -1.0))
        holds = int(np.sum(act == 0.0))
        net_flow = float(np.sum(act))

        outputs.append(SwarmTickOutput(
            **n.model_dump(),
            sentiment_score=float(sentiments[i]),
            simulated_price=float(prices[i]),
            buy_orders_count=buys,
            sell_orders_count=sells,
            hold_orders_count=holds,
            net_decision_flow=net_flow
        ))

    all_prices = [100.0] + prices
    return SwarmSimulationResponse(
        total_news_evaluated=len(news),
        overall_sentiment=round(float(np.mean(sentiments)), 4),
        final_simulated_price=float(prices[-1]),
        peak_simulated_price=float(np.max(all_prices)),
        trough_simulated_price=float(np.min(all_prices)),
        ticks=outputs
    )
