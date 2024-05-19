# crypto-volatility-detector/backend/fetch_data.py

import requests
import numpy as np

def fetch_coinbase_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,  # Fetch 1000 coins
        "page": 2,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        crypto_data = []
        for item in data:
            coin_data = {
                "name": item["name"],
                "symbol": item["symbol"],
                "current_price": item["current_price"],
                "market_cap": item["market_cap"],
                "price_change_percentage_1h_in_currency": item.get("price_change_percentage_1h_in_currency", 0),
                "price_change_percentage_24h": item["price_change_percentage_24h"]
            }
            # Fetch historical data for volatility calculation
            historical_data = fetch_historical_data(item["id"])
            if historical_data:
                coin_data["volatility"] = calculate_volatility(historical_data)
            else:
                coin_data["volatility"] = None
            crypto_data.append(coin_data)
        # Sort by 1-hour change in descending order
        crypto_data.sort(key=lambda x: x["price_change_percentage_1h_in_currency"], reverse=True)
        return crypto_data
    else:
        raise Exception("Error fetching data from CoinGecko API")

def fetch_historical_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "30",  # Fetch 30 days of data
        "interval": "daily"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        prices = [price[1] for price in data["prices"]]
        return prices
    else:
        return None

def calculate_volatility(prices):
    log_returns = np.diff(np.log(prices))
    volatility = np.std(log_returns) * np.sqrt(len(log_returns))
    return volatility

if __name__ == "__main__":
    # For testing purpose
    data = fetch_coinbase_data()
    for crypto in data:
        print(crypto)

