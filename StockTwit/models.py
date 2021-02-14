from . import db

class StockAnalysis(db.Document):
    tweets = db.EmbeddedDocumentField(TweetRequest)

class TweetRequest(db.EmbeddedDocument):
    raw_tweets = db.ListField(db.StringField())