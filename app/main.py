from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yfinance as yf
import firebase_admin
from firebase_admin import credentials, auth
from datetime import datetime, timedelta
import cachetools

# 🔹 Initialize Firebase Admin SDK
cred = credentials.Certificate("firebase/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

app = FastAPI()

# 🔹 Enable CORS for frontend (Next.js runs on localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # change to Vercel URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Request Model
class StockRequest(BaseModel):
    tickers: list[str]
    timeframe: str
    start_date: str | None = None
    end_date: str | None = None

# 🔹 Simple in-memory cache (5 min expiry)
cache = cachetools.TTLCache(maxsize=100, ttl=300)

# 🔹 Auth Dependency
async def verify_token(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    try:
        token = auth_header.split(" ")[1]
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid Firebase token")

# 🔹 Timeframe → Interval Mapping
def get_interval(timeframe: str):
    mapping = {
        "1D": "5m",
        "1W": "60m",
        "1M": "1d",
        "3M": "1d",
        "1Y": "1d",
        "YTD": "1d",
        "MTD": "1d",
    }
    return mapping.get(timeframe, "1d")

def get_date_range(timeframe: str):
    today = datetime.today()
    if timeframe == "1D":
        start = today - timedelta(days=1)
    elif timeframe == "1W":
        start = today - timedelta(weeks=1)
    elif timeframe == "1M":
        start = today - timedelta(days=30)
    elif timeframe == "3M":
        start = today - timedelta(days=90)
    elif timeframe == "1Y":
        start = today - timedelta(days=365)
    elif timeframe == "YTD":
        start = datetime(today.year, 1, 1)
    elif timeframe == "MTD":
        start = datetime(today.year, today.month, 1)
    else:
        start = today - timedelta(days=30)
    return start.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d")

# 🔹 Stock Fetch API
@app.post("/api/stocks/fetch")
async def fetch_stocks(request: StockRequest, user=Depends(verify_token)):
    cache_key = f"{tuple(request.tickers)}-{request.timeframe}-{request.start_date}-{request.end_date}"
    if cache_key in cache:
        return cache[cache_key]

    if request.start_date and request.end_date:
        start, end = request.start_date, request.end_date
    else:
        start, end = get_date_range(request.timeframe)

    interval = get_interval(request.timeframe)

    data = {}
    for ticker in request.tickers:
        try:
            df = yf.download(ticker, start=start, end=end, interval=interval, progress=False)
            df = df[["Close"]].reset_index()
            df["Date"] = df["Date"].astype(str)
            data[ticker] = df.to_dict(orient="records")
        except Exception as e:
            data[ticker] = {"error": str(e)}

    response = {"data": data, "start": start, "end": end, "interval": interval}
    cache[cache_key] = response
    return response

@app.get("/")
def root():
    return {"message": "Stock Analytics Backend is running 🚀"}

# 🔹 Test endpoint without auth (for debugging)
@app.post("/api/stocks/fetch-test")
async def fetch_stocks_test(request: StockRequest):
    cache_key = f"{tuple(request.tickers)}-{request.timeframe}-{request.start_date}-{request.end_date}"
    if cache_key in cache:
        return cache[cache_key]

    if request.start_date and request.end_date:
        start, end = request.start_date, request.end_date
    else:
        start, end = get_date_range(request.timeframe)

    interval = get_interval(request.timeframe)

    data = {}
    for ticker in request.tickers:
        try:
            df = yf.download(ticker, start=start, end=end, interval=interval, progress=False)
            df = df[["Close"]].reset_index()
            df["Date"] = df["Date"].astype(str)
            data[ticker] = df.to_dict(orient="records")
        except Exception as e:
            data[ticker] = {"error": str(e)}

    response = {"data": data, "start": start, "end": end, "interval": interval}
    cache[cache_key] = response
    return response
