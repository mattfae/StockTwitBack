import tweepy
from os import environ

CONSUMER_KEY = environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET_KEY = environ.get('TWITTER_CONSUMER_SECRET_KEY')

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
        self.tweet_dict = {}

    def get_tweets(self):
        for index, tweet in tweepy.Cursor(api.search, q=self.stock_symbol, until=self.open_date).items(10):
            print("printing tweet", tweet.text)
            self.tweet_dict[index] = tweet.text
