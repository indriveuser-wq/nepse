from fastapi import FastAPI
import requests

app = FastAPI()

BASE_URL = "https://nepsealpha.com/api/v1/market-summary"

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/prices")
def get_prices():
    try:
        res = requests.get(BASE_URL, timeout=10)

        print("Status:", res.status_code)

        if res.status_code == 200:
            data = res.json()

            # 🔥 FIX: correct data path
            return data.get("data", [])

    except Exception as e:
        return {"error": str(e)}

    return []