from . import db
from datetime import datetime

class Stock(db.Document):
    #pylint: disable=no-member
    created = db.DateTimeField()
    modified = db.DateTimeField(default=datetime.datetime.now())
    
    #Stock Symbol
    stock = db.StringField()
    #the open date to compare with the previous day's close
    open_date = db.DateTimeField()
    #tweets as taken directly from Twitter API
    raw_tweets = db.DictField()
    #tweets cleaned in preparation for analysis
    clean_tweets = db.ListField(db.StringField())
    #stock data taken from Alpha Vantage
    raw_stock_data = db.DictField()
    
    def save(self, *args, **kwargs):
        if not self.created:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        return super(TweetRequest, self).save(*args, **kwargs)

#class StockAnalysis(db.Document):
#    tweets = db.EmbeddedDocumentField(TweetRequest)
