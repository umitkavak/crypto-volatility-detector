from flask import Flask, jsonify
from .fetch_data import fetch_coinbase_data
from .calculate_metrics import calculate_volatility, calculate_bollinger_bands
from .sentiment_analysis import fetch_twitter_sentiment
from .news_aggregation import fetch_reddit_sentiment
from .database import get_db
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/volatile-coins', methods=['GET'])
def get_volatile_coins():
    coins = ['BTC', 'ETH', 'LTC', 'ADA', 'SOL']
    results = []

    for coin in coins:
        price = fetch_coinbase_data(coin)
        sentiment = fetch_twitter_sentiment(coin) + fetch_reddit_sentiment(coin)
        volatility = calculate_volatility(price)
        upper_band, lower_band = calculate_bollinger_bands(price)
        results.append({
            "coin": coin,
            "price": price,
            "volatility": volatility,
            "sentiment": sentiment,
            "bollinger_bands": {
                "upper_band": upper_band,
                "lower_band": lower_band
            }
        })

    return jsonify(results)
    
@app.route('/api/data')
def get_data():
    try:
        data = fetch_coinbase_data()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

