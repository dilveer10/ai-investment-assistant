def detect_trend(prices):
    if len(prices) < 2:
        return "not enough data"

    # Get just the closing prices (already sorted newest → oldest)
    closing_prices = [p["close"] for p in prices]
    change = closing_prices[-1] - closing_prices[0]
    pct_change = (change / closing_prices[0]) * 100

    if pct_change > 2:
        return "uptrend"
    elif pct_change < -2:
        return "downtrend"
    else:
        return "flat"
