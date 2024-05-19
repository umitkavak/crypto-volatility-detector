import os

# List of directories and files to be created
structure = [
    "crypto-volatility-detector/backend/__init__.py",
    "crypto-volatility-detector/backend/fetch_data.py",
    "crypto-volatility-detector/backend/calculate_metrics.py",
    "crypto-volatility-detector/backend/sentiment_analysis.py",
    "crypto-volatility-detector/backend/news_aggregation.py",
    "crypto-volatility-detector/backend/database.py",
    "crypto-volatility-detector/backend/config.py",
    "crypto-volatility-detector/backend/app.py",
    "crypto-volatility-detector/frontend/public/",
    "crypto-volatility-detector/frontend/src/components/",
    "crypto-volatility-detector/frontend/src/App.js",
    "crypto-volatility-detector/frontend/src/index.js",
    "crypto-volatility-detector/frontend/src/styles.css",
    "crypto-volatility-detector/frontend/package.json",
    "crypto-volatility-detector/frontend/.babelrc",
    "crypto-volatility-detector/frontend/webpack.config.js",
    "crypto-volatility-detector/requirements.txt",
    "crypto-volatility-detector/run_backend.sh",
    "crypto-volatility-detector/run_frontend.sh",
    "crypto-volatility-detector/README.md",
]

for item in structure:
    if item.endswith('/'):
        # Create directory
        os.makedirs(item, exist_ok=True)
        print(f"Created directory: {item}")
    else:
        # Create file and ensure the directory exists
        directory = os.path.dirname(item)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            print(f"Created directory: {directory}")
        with open(item, 'w') as f:
            pass
        print(f"Created file: {item}")

