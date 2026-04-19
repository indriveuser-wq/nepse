from fastapi import FastAPI
import requests
import time

app = FastAPI()

HEADERS = {"User-Agent": "Mozilla/5.0"}

CACHE = {"data": [], "timestamp": 0}


def fetch_nepsealpha():
    try:
        res = requests.get(
            "https://nepsealpha.com/api/v1/market-summary",
            headers=HEADERS,
            timeout=5
        )
        if res.status_code == 200:
            return res.json().get("data", [])
    except:
        return None


def fetch_static():
    return [
        {"symbol": "NABIL", "lastTradedPrice": 450},
        {"symbol": "NTC", "lastTradedPrice": 800},
        {"symbol": "NRIC", "lastTradedPrice": 1200},
        {"symbol": "GBIME", "lastTradedPrice": 320},
        {"symbol": "ADBL", "lastTradedPrice": 290},
    ]


def get_data():
    data = fetch_nepsealpha()

    if data:
        CACHE["data"] = data
        return data

    print("Using fallback data")
    return fetch_static()


@app.get("/")
def home():
    return {"status": "ok"}


@app.get("/prices")
def prices():
    return get_data()