
import requests

API_KEY = "HZU9MHINIZ6URRA1"  # Replace with your actual key
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
        clean_data =[]

        for date, values in list(raw_prices.items())[:10]:
            close_price = values["4. close"]
            clean_data.append({
                "date": date,
                "close": float(close_price)
            })

        return {"symbol": symbol.upper(), "prices": clean_data}
    
    except KeyError:
        return {"error": "Invalid symbol or API LIMIT HAS BEEN REACHED"}
    

    
