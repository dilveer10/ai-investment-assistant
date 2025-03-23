import requests
from utils.trend_analyzer import detect_trend

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://www.alphavantage.co/query"

def get_stock_data(symbol):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    try:
        raw_prices = data["Time Series (Daily)"]
        clean_data = []

        for date, values in list(raw_prices.items())[:10]:
            close_price = values["4. close"]
            clean_data.append({
                "date": date,
                "close": float(close_price)
            })

        trend = detect_trend(clean_data)  # 🧠 Call AI function here

        return {
            "symbol": symbol.upper(),
            "prices": clean_data,
            "trend": trend  # 👈 Include in the response
        }

    except KeyError:
        return {"error": "Invalid symbol or API limit reached"}
