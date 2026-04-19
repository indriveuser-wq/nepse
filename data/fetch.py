import requests

BASE_URL = "https://nepsealpha.com/api/v1/trading-today"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
}

_cached_data = None


def fetch_all_prices():
    try:
        res = requests.get(BASE_URL, headers=HEADERS, timeout=10)

        print("NepseAlpha status:", res.status_code)

        if res.status_code == 200:
            return res.json()

    except Exception as e:
        print("Error:", e)

    return []


def get_live_price(symbol):
    global _cached_data

    if _cached_data is None:
        _cached_data = fetch_all_prices()

    if not _cached_data:
        return None

    for stock in _cached_data:
        if stock.get("symbol") == symbol:
            try:
                return float(stock.get("lastTradedPrice", 0))
            except:
                return None

    return None