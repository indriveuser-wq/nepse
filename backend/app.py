from fastapi import FastAPI
import requests
import time

app = FastAPI()

HEADERS = {"User-Agent": "Mozilla/5.0"}

# cache
CACHE = {
    "data": [],
    "timestamp": 0
}
CACHE_TTL = 300  # 5 minutes


# -------------------------------
# SOURCE 1 (primary - may fail)
# -------------------------------
def fetch_nepsealpha():
    try:
        res = requests.get(
            "https://nepsealpha.com/api/v1/market-summary",
            headers=HEADERS,
            timeout=5
        )
        if res.status_code == 200:
            data = res.json()
            return data.get("data", [])
    except Exception as e:
        print("NepseAlpha failed:", e)
    return None


# -------------------------------
# SOURCE 2 (fallback - static JSON)
# -------------------------------
def fetch_static():
    try:
        res = requests.get(
            "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.json",
            timeout=5
        )
        if res.status_code == 200:
            data = res.json()

            # simulate price
            result = []
            for i, stock in enumerate(data[:50]):
                result.append({
                    "symbol": stock["Symbol"],
                    "lastTradedPrice": 100 + i * 5
                })
            return result
    except Exception as e:
        print("Static fallback failed:", e)

    return None


# -------------------------------
# MAIN LOGIC (like repo)
# -------------------------------
def get_data():
    # 1. try fresh sources
    for source in [fetch_nepsealpha, fetch_static]:
        data = source()
        if data:
            CACHE["data"] = data
            CACHE["timestamp"] = time.time()
            return data

    # 2. fallback to cache
    if CACHE["data"]:
        print("Using cached data")
        return CACHE["data"]

    return []


@app.get("/")
def home():
    return {"status": "ok"}


@app.get("/prices")
def prices():
    return get_data()