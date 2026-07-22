# Multi-Agent AI Financial Market Trading Swarm & Sentiment Engine — Technical Guide

Welcome to the technical and educational guide for the **Multi-Agent AI Financial Market Trading Swarm & Sentiment Engine**. This document details agent utility functions, news sentiment vector calculations, price discovery equations, and client interview pitch points.

---

## 1. Executive Summary: What Problem Does This Solve?

### In Plain English
Financial news feeds (Twitter/X, Bloomberg, Reuters) release thousands of headlines daily. How does this aggregate sentiment translate into actual buying and selling decisions in the market?

This engine simulates a swarm of **Autonomous AI Trading Agents**, each with a distinct risk aversion profile, expected return baseline, and sentiment sensitivity. The agents read news headlines in real time, calculate their action utility, and execute trades that collectively drive market price movements.

---

## 2. Mathematical & Agentic Formulations

### 1. Agent Decision Utility Function ($U_i$)
Each agent $i$ chooses between buying ($+1$), selling ($-1$), or holding ($0$) by evaluating:

$$U_i(\text{action}) = \text{Expected Return}_i + \beta_i \cdot \text{Sentiment}_t - \gamma_i \cdot \text{Variance}_i$$

- $\beta_i$: Agent's sensitivity to news sentiment.
- $\gamma_i$: Agent's risk aversion coefficient.
- $\text{Sentiment}_t$: Parsed NLP news sentiment score.

---

### 2. Market Price Discovery Engine
The simulated market price $P_t$ adjusts based on the aggregate net order flow imbalance of the active AI agent swarm:

$$P_t = P_{t-1} \cdot \left(1 + \eta \cdot \sum_{i=1}^N \text{Order}_i + \sigma \cdot \epsilon\right)$$

- $\eta$: Price impact parameter ($0.02$).
- $\sum \text{Order}_i$: Net swarm order flow (number of buys minus number of sells).
- $\sigma \cdot \epsilon$: Volatility noise.

---

## 3. Architecture & Tech Stack

```
ai-agent-swarm-simulator/
├── index.html                   # Standalone Live Dashboard (AI Swarm Terminal)
├── test_sentiment_news_dataset.csv # Sample news sentiment CSV
├── backend/
│   ├── app/
│   │   ├── analytics/
│   │   │   ├── agent_swarm_engine.py    # Vectorized Agent Swarm decision utility engine
│   │   │   └── sentiment_parser.py      # Rule-based NLP sentiment parser
│   │   ├── api/
│   │   │   └── endpoints.py    # FastAPI REST routes & CSV uploader
│   │   └── main.py             # FastAPI entry point
│   └── tests/
│       └── test_swarm_engine.py  # Pytest unit test suite
```

---

## 4. Client Pitch & Interview Talking Points

1. **"What business ROI does this multi-agent simulation deliver?"**
   > *"It allows financial firms and asset managers to model market sentiment spikes, run what-if stress tests of news headlines, and simulate liquidity responses under extreme trading conditions."*

2. **"What makes the UI/UX different and unique?"**
   > *"It features a 60 FPS HTML5 Canvas animated neural network background representing active agent communications, coupled with interactive Chart.js price trajectory curves."*
