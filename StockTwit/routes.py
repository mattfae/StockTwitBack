from flask import Response, request
from flask import current_app as app
from .models import TweetRequest


@app.route('/tweets/', methods=['GET', 'POST'])
def get_tweets():
    if request.method == 'GET':
        print("starting get_tweets")
        tweets = TweetRequest.objects().to_json()
        return Response(tweets, mimetype="application/json", status=200)

    elif request.method == 'POST':
        print("starting add_tweets")
        body = request.get_json()
        tweets = TweetRequest(**body)
        tweets.save()
        id = tweets.id
        return {'id': str(id)}, 200
