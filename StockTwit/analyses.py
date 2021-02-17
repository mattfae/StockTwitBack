import tweepy
from decouple import config

CONSUMER_KEY = config('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET_KEY = config('TWITTER_CONSUMER_SECRET_KEY')

tweepy_auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
api = tweepy.API(tweepy_auth)

class StockTweets:
    """
    a collection of tweets taken from the Twitter API based on a given date
    StockTweets(self, stock_symbol: str)
    """
    def __init__(self, _stock_symbol, _open_date):
        self.stock_symbol = f'${_stock_symbol}'
        self.open_date = _open_date
        self.tweets = list()

    def get_tweets(self):
        for tweet in tweepy.Cursor(api.search, q=self.stock_symbol, until=self.open_date, count=10):
            print("printing tweet", tweet.text)
            self.tweets.append(tweet.text)
