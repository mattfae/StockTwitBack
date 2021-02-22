from . import db
from datetime import datetime

class TweetRequest(db.Document):
    #pylint: disable=no-member
    created = db.DateTimeField()
    modified = db.DateTimeField(default=datetime.datetime.now())
    
    stock = db.StringField()
    open_date = db.DateTimeField()
    raw_tweets = db.ListField(db.StringField())
    raw_av_data = db.DictField()

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        return super(TweetRequest, self).save(*args, **kwargs)

#class StockAnalysis(db.Document):
#    tweets = db.EmbeddedDocumentField(TweetRequest)
