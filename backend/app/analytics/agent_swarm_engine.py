"""
Vectorized Multi-Agent AI Swarm & Price Discovery Simulation Engine using NumPy.
"""

import numpy as np
from typing import Dict, Any, List

def simulate_agent_swarm_decisions(
    news_sentiment_scores: np.ndarray,
    baseline_returns: np.ndarray,
    risk_aversion_coefficients: np.ndarray,
    sentiment_sensitivities: np.ndarray,
    initial_price: float = 100.0,
    impact_multiplier: float = 0.02
) -> Dict[str, Any]:
    """
    Simulates autonomous AI trading agent decisions (Buy/Sell/Hold) based on utility curves.
    """
    s = np.asarray(news_sentiment_scores, dtype=np.float64)
    r = np.asarray(baseline_returns, dtype=np.float64)
    gamma = np.asarray(risk_aversion_coefficients, dtype=np.float64)
    beta = np.asarray(sentiment_sensitivities, dtype=np.float64)

    n = len(s)
    prices = [initial_price]
    agent_actions = []  # List of arrays containing decisions for each step

    for t in range(n):
        # Calculate utility for buying (+1 expected return) vs selling (-1 expected return)
        sentiment_signal = s[t]
        
        # Utility of buying: expected return + sentiment boost - risk penalty
        u_buy = r + (beta * sentiment_signal) - (gamma * 0.05)
        # Utility of selling: -expected return - sentiment drag - risk penalty
        u_sell = -r - (beta * sentiment_signal) - (gamma * 0.05)

        # Decision rule: Buy = 1 (if u_buy > u_sell and u_buy > 0.0), Sell = -1 (if u_sell > u_buy and u_sell > 0.0), else Hold = 0
        buy_cond = (u_buy > u_sell) & (u_buy > 0.0)
        sell_cond = (u_sell > u_buy) & (u_sell > 0.0)
        
        actions = np.zeros_like(r)
        actions = np.where(buy_cond, 1.0, actions)
        actions = np.where(sell_cond, -1.0, actions)
        agent_actions.append(actions)

        # Aggregate swarm order flow imbalance
        net_order_flow = float(np.sum(actions))
        
        # Price Discovery Equation
        current_price = prices[-1]
        next_price = current_price * (1.0 + (impact_multiplier * net_order_flow) + np.random.normal(0, 0.002))
        prices.append(round(next_price, 4))

    return {
        "prices": prices[1:],
        "decisions": agent_actions
    }
