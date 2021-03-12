import tweepy
import requests
import json
from datetime import datetime, timedelta
from decouple import config
import sent_analyzer as sa
import pdb


CONSUMER_KEY = config('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET_KEY = config('TWITTER_CONSUMER_SECRET_KEY')
AV_API_KEY = config('AV_API_KEY')

tweepy_auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
api = tweepy.API(tweepy_auth)


class StockAnalysis:
    """
    a collection of tweets taken from the Twitter API based on a given date
    StockAnalysis(self, stock_symbol: str, open_date: str)
    """
    def __init__(self, _stock_symbol, _open_date):
        self.stock_symbol = _stock_symbol
        self.open_date = datetime.strptime(_open_date, '%Y-%m-%d')
        self.close_date = self.open_date - timedelta(days=1)
        self.raw_tweet_data = list()
        self.scored_tweets = list()
        self.market_data = None


    def get_tweets(self):
        #use tweepy to geat relevant tweets
        print("starting get_tweets")
        for tweet in tweepy.Cursor(api.search, q=f'${self.stock_symbol}', until=self.open_date.strftime("%Y-%m-%d"), count=5).items(5):
            self.raw_tweet_data.append(tweet)


    def analyze_tweets(self):
        tweets = [tweet.text for tweet in self.raw_tweet_data]
        self.scored_tweets = list(map(sa.process_tweet, tweets))


    def get_market_data(self):
        print(f'starting request for {self.stock_symbol} using {AV_API_KEY}.')
        try:
            resp_data = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.stock_symbol}&apikey={AV_API_KEY}')
        except requests.exceptions.ConnectionError:
            print("Connection refused")
        
        self.market_data = json.loads(resp_data.content.decode('utf-8'))


pdb.set_trace()
#new = StockAnalysis('aapl', '2021-03-10')
#okay
