from flask import Response, request, jsonify
from flask import current_app as app
from .analyses import StockTweets
from .models import TweetRequest


@app.route('/stocks/', methods=['GET'])
def get_all():
    if request.method == 'GET':
        print("starting old_request")
        tweets = TweetRequest.objects()
        return jsonify(tweets)


@app.route('/stocks/<string:stock>', methods=['GET'])
def get_stock_results(stock):
    if request.method == 'GET':
        print("starting old_request")
        tweets = TweetRequest.objects()
        return jsonify(tweets)


@app.route('/stocks/<string:stock>/<string:date>', methods=['GET', 'POST'])
def get_stock_date(stock):
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
