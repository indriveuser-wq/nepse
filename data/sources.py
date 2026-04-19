from bs4 import BeautifulSoup
from utils.proxy import safe_request


# 🟢 MeroLagani (robust version)
def fetch_merolagani(symbol):
    url = f"https://merolagani.com/CompanyDetail.aspx?symbol={symbol}"

    try:
        res = safe_request(url, {"Referer": "https://merolagani.com/"})

        if not res:
            print("MeroLagani: no response")
            return None

        print("MeroLagani status:", res.status_code)

        if res.status_code != 200:
            return None

        soup = BeautifulSoup(res.text, "html.parser")

        # 🔍 Try multiple selectors (more robust)
        selectors = [
            ".market-price",
            "#ctl00_ContentPlaceHolder1_lblMarketPrice",
            ".price",
        ]

        for sel in selectors:
            tag = soup.select_one(sel)
            if tag:
                try:
                    price = tag.text.strip().replace(",", "")
                    return float(price)
                except:
                    continue

        print("MeroLagani: price not found")

    except Exception as e:
        print("MeroLagani error:", e)

    return None


# 🔵 NepseAlpha (fixed + safe)
def fetch_nepsealpha(symbol):
    url = f"https://nepsealpha.com/api/v1/stock/{symbol}"

    try:
        res = safe_request(url, {"Accept": "application/json"})

        if not res:
            print("NepseAlpha: no response")
            return None

        print("NepseAlpha status:", res.status_code)

        if res.status_code != 200:
            return None

        data = res.json()

        # Try multiple possible keys
        possible_keys = [
            "lastTradedPrice",
            "ltp",
            "close",
        ]

        for key in possible_keys:
            if key in data:
                return float(data[key])

        print("NepseAlpha: price key not found")

    except Exception as e:
        print("NepseAlpha error:", e)

    return None