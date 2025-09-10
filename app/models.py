# app/models.py
from pydantic import BaseModel
from typing import List, Optional

class FetchRequest(BaseModel):
    tickers: List[str]
    period: Optional[str] = None  # '1d','5d','1mo', '3mo', '1y' etc
    interval: Optional[str] = None  # '1m','5m','60m','1d'
    start: Optional[str] = None  # ISO date yyyy-mm-dd
    end: Optional[str] = None
