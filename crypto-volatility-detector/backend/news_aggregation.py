import praw
from .config import Config

def fetch_reddit_sentiment(coin):
    reddit = praw.Reddit(client_id=Config.REDDIT_CLIENT_ID,
                         client_secret=Config.REDDIT_CLIENT_SECRET,
                         user_agent='crypto-volatility-detector')
    submissions = reddit.subreddit('cryptocurrency').search(coin, limit=100)
    sentiment_score = sum([TextBlob(submission.title).sentiment.polarity for submission in submissions]) / len(submissions)
    return sentiment_score
