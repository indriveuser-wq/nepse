import requests
import random

SESSION = requests.Session()

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
]

def get_headers(extra=None):
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "en-US,en;q=0.9",
    }
    if extra:
        headers.update(extra)
    return headers


def safe_request(url, extra_headers=None, timeout=10):
    try:
        headers = get_headers(extra_headers)
        res = SESSION.get(url, headers=headers, timeout=timeout)
        return res
    except Exception as e:
        print("Request failed:", e)
        return None