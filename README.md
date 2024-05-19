# Crypto Volatility Detector

The Crypto Volatility Detector is a web application that fetches real-time cryptocurrency data, calculates volatility, and displays the data in a user-friendly interface. This project uses Flask for the backend to fetch data from the CoinGecko API and React for the frontend to display the data.

## Features

- Fetches real-time cryptocurrency data from CoinGecko API
- Calculates the volatility of each cryptocurrency based on historical price data
- Displays the data in a tabular format with parameters like current price, market cap, 1-hour change, 24-hour change, and 30-day volatility

## Project Structure

<img width="216" alt="Screenshot 2024-05-19 at 11 51 01" src="https://github.com/umitkavak/crypto-volatility-detector/assets/26542534/f45ef5bc-87b9-4f74-92e6-0df0bb4b6188">


## Setup Instructions

### Backend Setup

1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   
3. **Run the backend server:**
   ```bash
   chmod +x run_backend.sh
   ./run_backend.sh


### Frontend Setup
Navigate to the frontend directory:

1.  ```bash
    cd frontend
2. Install the required dependencies:
     ```bash
      npm install

3. Run the frontend development server:
     ```bash
     chmod +x run_frontend.sh
     ./run_frontend.sh

### Usage
To start both backend and frontend servers, type 

**Backend**: 

     ./run_backend.sh

in one terminal, and

**Frontend**:

    ./run_frontend.sh

in another terminal. 

Access the frontend application:
Open a browser and navigate to http://localhost:9000

See image below for the result: 
![WhatsApp Image 2024-05-15 at 18 17 49](https://github.com/umitkavak/crypto-volatility-detector/assets/26542534/90743ac7-f44b-461e-a08e-d6962e334296)
