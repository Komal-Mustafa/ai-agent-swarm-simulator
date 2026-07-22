# SwarmPulse — Multi-Agent AI Financial Trading Swarm & Sentiment Engine 🚀

An enterprise-grade **Multi-Agent AI Financial Trading Swarm & News Sentiment Engine** featuring a **60 FPS HTML5 Canvas animated agent mesh background**, vectorized **NumPy** agent utility curves, rule-based NLP news sentiment vectorization, and simulated market price discovery.

---

## 🌟 Key Features

- **Animated Agent Swarm Network**: High-performance 60 FPS HTML5 Canvas animation displaying floating agent nodes that flash and communicate via pulsing laser vectors during sentiment swings.
- **Agentic Swarm Decision Core**: Vectorized expected utility modeling ($U(a) = \mathbb{E}[R] + \beta S - \gamma \text{Var}(R)$) for hundreds of autonomous agents.
- **Rule-Based NLP Lexicon Parser**: Categorizes Bloomberg/Twitter news headlines into normalized sentiment vectors.
- **Universal News CSV Ingestion**: Support for custom news datasets (`headline`, `impact_weight`).

---

## 🚀 Quick Start Guide

### 1. Launch Live Web App (Zero Setup)
```bash
cd ai-agent-swarm-simulator
python -m http.server 8006
```
Open **`http://localhost:8006`** in your browser!

### 2. Launch FastAPI REST Server
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8006
```
API Documentation live at `http://localhost:8006/docs`.

### 3. Run Pytest Test Suite
```bash
cmd /c "set PYTHONPATH=backend && python -m pytest backend/tests"
```

---

## 📖 Educational Documentation

For complete multi-agent utility math derivations, sentiment vector rules, and quantitative interview pitch points, read **[PROJECT_EXPLAINER.md](file:///C:/Users/Shahab%20Ahmad/.gemini/antigravity/scratch/ai-agent-swarm-simulator/PROJECT_EXPLAINER.md)**.
