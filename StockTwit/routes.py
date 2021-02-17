from flask import Response, request
from flask import current_app as app
from .analyses import StockTweets
from .models import TweetRequest


@app.route('/tweets/', methods=['GET', 'POST'])
def get_tweets():
    if request.method == 'GET':
        print("starting old_request")
        tweets = TweetRequest.objects().to_json()
        return Response(tweets, mimetype="application/json", status=200)

    elif request.method == 'POST':
        print("starting new_request")
        tweet_holder = StockTweets("PLTR", "2021-02-16")
        tweet_holder.get_tweets
        print("printing tweetholder", tweet_holder.tweet_dict)
        #parsed = TweetRequest(**body)
        #parsed.save()
        #id = parsed.id
        return Response(tweet_holder.tweet_dict, mimetype="application/json", status=200)
