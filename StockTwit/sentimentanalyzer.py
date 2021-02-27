import re, string


def remove_noise(tweet):
    tweet = tweet.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', tweet)
    tweet = tweet.sub("(@[A-Za-z0-9_]+)","", tweet))
    return tweet



print(twitter_samples)

