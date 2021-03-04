import re
from nltk import sent_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def clean_tweet(tweet):
    tweet = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', tweet)
    return re.sub("(@[A-Za-z0-9_]+)","", tweet)
    

def get_sentence_sentiment(sentence):
    sia = SentimentIntensityAnalyzer()
    return (f'"{sentence}": {sia.polarity_scores(sentence)}')


def process_tweets(tweets):
    sentences = []
    for tweet in tweets:
        for item in sent_tokenize(clean_tweet(tweet)):
            sentences.append(get_sentence_sentiment(item))
    return sentences
