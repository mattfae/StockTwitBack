from nltk import sent_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


    def tokenize_tweets(tweets):
        all_sentences = []
        for tweet in tweets:
            all_sentences += sent_tokenize(tweet)
        return all_sentences


    def analyze_tweets(tweets):
        sia = SentimentIntensityAnalyzer()
        tweets_with_scores = list()

        for tweet in tweets:
            tw_scores = sia.polarity_scores(tweet)
            tweet_with_scores.append((tweet, tw_scores))
        
        return tweets_with_scores
