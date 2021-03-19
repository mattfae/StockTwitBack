from stocktwit import create_app
from stocktwit.models import StockTweet
import pdb

app = create_app()

pdb.set_trace()

if __name__ == "__main__":
    app.run(debug=True)
