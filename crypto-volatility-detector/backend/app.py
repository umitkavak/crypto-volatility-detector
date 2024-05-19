from flask import Flask, jsonify
from flask_cors import CORS
from backend.fetch_data import fetch_coinbase_data


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/data')
def get_data():
    try:
        data = fetch_coinbase_data()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

