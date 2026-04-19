from fastapi import FastAPI
import requests

app = FastAPI()

DATA_URL = "https://raw.githubusercontent.com/indriveuser-wq/nepse/main/data.json"

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/prices")
def get_prices():
    try:
        res = requests.get(DATA_URL, timeout=10)

        if res.status_code == 200:
            return res.json()

    except Exception as e:
        return {"error": str(e)}

    return []