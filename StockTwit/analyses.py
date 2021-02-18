import tweepy
import requests
import json
import pdb
from decouple import config

CONSUMER_KEY = config('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET_KEY = config('TWITTER_CONSUMER_SECRET_KEY')
POLYGON_API_KEY = config('POLYGON_API_KEY')

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
        self.close_price = None
        self.open_price = None

    def get_tweets(self):
        #use tweepy to geat relevant tweets
        print("starting get_tweets")
        for tweet in tweepy.Cursor(api.search, q=self.stock_symbol, until=self.open_date, count=10).items(10):
            print("printing tweet", tweet.text)
            self.tweets.append(tweet.text)

    def get_close_open(self):
        close_response = requests.get('https://api.polygon.io/v1/open-close/AAPL/2020-10-14?unadjusted=false&apiKey=Ua0sj7CCQxDQfCXLVp34CFUKWyVCWL99')
        self.close_price = json.loads(close_response.content.decode('utf-8'))["close"]
        
        open_response = requests.get('https://api.polygon.io/v1/open-close/AAPL/2020-10-14?unadjusted=false&apiKey=Ua0sj7CCQxDQfCXLVp34CFUKWyVCWL99')
        self.open_price = json.loads(open_response.content.decode('utf-8'))["open"]

pdb.set_trace()
#new = StockTweets('aapl', '2021-02-18')
