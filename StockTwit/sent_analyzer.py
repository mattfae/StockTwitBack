import re
from nltk import sent_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def clean_tweet(tweet):
    tweet = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', tweet)
    return re.sub("(@[A-Za-z0-9_]+)","", tweet)
    

def get_sentence_sentiment(sentence):
    sia = SentimentIntensityAnalyzer()
    return {
        sentence : sia.polarity_scores(sentence)
        }


def process_tweet(tweet):
    #clean tweetn, then 
    return get_sentence_sentiment(clean_tweet(tweet))
