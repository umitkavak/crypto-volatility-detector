import tweepy
from .config import Config
from textblob import TextBlob

def fetch_twitter_sentiment(coin):
    auth = tweepy.OAuth1UserHandler(Config.TWITTER_API_KEY)
    api = tweepy.API(auth)
    tweets = api.search(q=coin, count=100, lang='en')
    sentiment_score = sum([TextBlob(tweet.text).sentiment.polarity for tweet in tweets]) / len(tweets)
    return sentiment_score
