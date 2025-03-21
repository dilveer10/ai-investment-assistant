
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
    return data
