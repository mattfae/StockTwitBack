import nltk
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag


positive_tweets = twitter_samples.strings('positive_tweets.json')

tweet_tokens = twitter_samples.tokenized('positive_tweets.json')[0]

print(pos_tag(tweet_tokens))