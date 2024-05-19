# Crypto Volatility Detector

This project aims to detect and analyze the volatility of various cryptocurrencies using data fetched from different sources and performing sentiment analysis on related news and social media content.

## Project Structure

- `backend/`: Contains server-side scripts and logic.
  - `fetch_data.py`: Fetch cryptocurrency data from APIs.
  - `calculate_metrics.py`: Calculate volatility and other financial metrics.
  - `sentiment_analysis.py`: Perform sentiment analysis on news and social media.
  - `news_aggregation.py`: Aggregate news from different sources.
  - `database.py`: Manage database connections and operations.
  - `config.py`: Configuration settings.
  - `app.py`: Main application file.
  
- `frontend/`: Contains client-side code.
  - `public/`: Public assets.
  - `src/`: Source code for the React application.
    - `components/`: React components.
    - `App.js`: Main React component.
    - `index.js`: Entry point for React.
    - `styles.css`: Stylesheet.
  - `package.json`: Frontend dependencies and scripts.
  - `.babelrc`: Babel configuration.
  - `webpack.config.js`: Webpack configuration.

- `requirements.txt`: Backend dependencies.
- `run_backend.sh`: Script to start the backend server.
- `run_frontend.sh`: Script to start the frontend server.
- `README.md`: Project documentation.

## Setup Instructions

### Backend

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

