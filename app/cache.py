# app/cache.py
from cachetools import TTLCache, cached
from typing import Tuple

# cache key: (tickers_tuple, start, end, interval)
CACHE = TTLCache(maxsize=500, ttl=600)  # default TTL 10 minutes

def cache_decorator(fn):
    return cached(CACHE)(fn)
