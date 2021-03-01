import re, string
from nltk import sent_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def remove_noise(tweet):
    tweet = tweet.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', tweet)
    tweet = tweet.sub("(@[A-Za-z0-9_]+)","", tweet)
    return tweet


def tokenize_tweets(tweets):
    all_sentences = []
    for tweet in tweets:
        all_sentences += sent_tokenize(tweet)
    return all_sentences


def analyze_tweets(tweet):
    sia = SentimentIntensityAnalyzer()

    sentiment_results = sia.polarity_scores(tweet)
