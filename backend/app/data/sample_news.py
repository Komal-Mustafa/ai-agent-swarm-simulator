"""
Sample Bloomberg/X financial news headlines with sentiment indicators.
"""

from typing import List, Dict, Any

SAMPLE_NEWS: List[Dict[str, Any]] = [
    { "news_id": "NEWS-001", "headline": "Al Rajhi Bank reports 15% profit growth in Q2 approved reports", "impact_weight": 1.2 },
    { "news_id": "NEWS-002", "headline": "SAMA announces open banking sandbox expansion for strategic FinTech", "impact_weight": 1.5 },
    { "news_id": "NEWS-003", "headline": "Regulatory fine warning issued to regional lending firms", "impact_weight": 0.8 },
    { "news_id": "NEWS-004", "headline": "Dubai DIFC sees surge in quantitative hedge fund registrations", "impact_weight": 1.4 },
    { "news_id": "NEWS-005", "headline": "Regional inflation index drops to target range following policy review", "impact_weight": 1.1 }
]
