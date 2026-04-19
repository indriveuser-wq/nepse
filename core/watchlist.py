import json
import os

FILE = "watchlist.json"


def load_watchlist():
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except:
        return []


def save_watchlist(data):
    with open(FILE, "w") as f:
        json.dump(data, f)


def add_stock(symbol):
    wl = load_watchlist()
    if symbol not in wl:
        wl.append(symbol)
        save_watchlist(wl)


def remove_stock(symbol):
    wl = load_watchlist()
    wl = [s for s in wl if s != symbol]
    save_watchlist(wl)