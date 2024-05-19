import numpy as np

def calculate_volatility(prices):
    return np.std(prices)

def calculate_bollinger_bands(prices, window=20, num_std_dev=2):
    rolling_mean = np.mean(prices[-window:])
    rolling_std = np.std(prices[-window:])
    upper_band = rolling_mean + (rolling_std * num_std_dev)
    lower_band = rolling_mean - (rolling_std * num_std_dev)
    return upper_band, lower_band
