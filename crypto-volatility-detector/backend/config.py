import os

class Config:
    COINBASE_API_URL = "https://api.coinbase.com/v2/prices"
    DB_URI = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/crypto_db")
    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
    REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
    REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
