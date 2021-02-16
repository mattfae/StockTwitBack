

class StockTweets(object):

    def __init__(self, ):
        

    api = tweepy.API(auth)
    for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
        self.tweets += tweet.text
