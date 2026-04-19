import statistics

def resolve_price(prices):
    prices = [p for p in prices if p is not None]

    if not prices:
        return None

    return round(statistics.median(prices), 2)