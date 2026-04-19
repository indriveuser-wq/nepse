from fastapi import FastAPI
import requests

app = FastAPI()

BASE_URL = "https://nepsealpha.com/api/v1/trading-today"

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/prices")
def get_prices():
    try:
        res = requests.get(BASE_URL, timeout=10)
        if res.status_code == 200:
            return res.json()
    except Exception as e:
        return {"error": str(e)}

    return []