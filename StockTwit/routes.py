from flask import Response, request
from flask import current_app as app
from models import 

"""
@app.route('/tweets/', methods=['GET', 'POST'])
def get_tweets():
    if methods == 'GET':
        print("starting get_tweets")
        goals = Goal.objects().to_json()
        return Response(goals, mimetype="application/json", status=200)

   elif methods == 'POST':
        print("starting add_tweets")
        body = request.get_json()
        goal = Goal(**body).save()
        id = goal.id
        return {'id': str(id)}, 200
"""