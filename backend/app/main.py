"""
Multi-Agent AI Financial Market Trading Swarm & Sentiment Engine — FastAPI Entry Point.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import router as api_router

app = FastAPI(
    title="Multi-Agent AI Financial Trading Swarm API",
    description="Vectorized Agent Utility Curves, News Sentiment NLP Parser & Price Discovery Swarm Simulator.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8006, reload=True)
