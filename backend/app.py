from fastapi import FastAPI
import requests

app = FastAPI()

SCRAPER_API_KEY = "7a75bde7c78f8035db7ddf321bc67f98"

TARGET_URL = "https://nepsealpha.com/api/v1/market-summary"


@app.get("/")
def home():
    return {"status": "ok"}


@app.get("/prices")
def get_prices():
    try:
        url = f"http://api.scraperapi.com?api_key={SCRAPER_API_KEY}&url={TARGET_URL}"

        res = requests.get(url, timeout=15)

        print("Status:", res.status_code)

        if res.status_code == 200:
            data = res.json()
            return data.get("data", [])

    except Exception as e:
        return {"error": str(e)}

    return []