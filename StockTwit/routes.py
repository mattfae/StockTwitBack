from flask import Response, request, jsonify
from flask import current_app as app
from .stocktweets import StockTweet
from .models import StockTweet
import .sent_analyzer as sa


@app.route('/stocks/', methods=['GET'])
def get_all():
    if request.method == 'GET':
        print("starting old_request")
        tweets = Stock.objects()
        return jsonify(tweets)


@app.route('/stocks/<string:stock>', methods=['GET'])
def get_stock_results(stock):
    if request.method == 'GET':
        print("starting old_request")
        tweets = Stock.objects()
        return jsonify(tweets)


@app.route('/stocks/<string:stock>/<string:date>', methods=['GET', 'POST'])
def get_stock_date(stock):
    if request.method == 'GET':
        print("starting old_request")
        tweets = StockTweet.objects()
        return jsonify(tweets)

    elif request.method == 'POST':
        data = request.json
        print("new request body:", data)
        #parsed = StockTweet(**body)
        #parsed.save()
        #id = parsed.id
        return jsonify(data)
