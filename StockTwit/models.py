from . import db

class TweetRequest(db.Document):
    #pylint: disable=no-member
    raw_tweets = db.ListField(db.StringField())

#class StockAnalysis(db.Document):
#    tweets = db.EmbeddedDocumentField(TweetRequest)
