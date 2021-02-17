from flask import Response, request, jsonify
from flask import current_app as app
from .analyses import StockTweets
from .models import TweetRequest

@app.route('/tweets/', methods=['GET', 'POST'])
def get_tweets():
    if request.method == 'GET':
        print("starting old_request")
        tweets = TweetRequest.objects()
        return jsonify(tweets)

    elif request.method == 'POST':
        data = request.json
        print("new request body:", data)
        #parsed = TweetRequest(**body)
        #parsed.save()
        #id = parsed.id
        return jsonify(data)
