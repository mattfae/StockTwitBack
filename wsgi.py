from stocktwit import create_app
import stocktwit
import pdb

app = create_app()


new = stocktwit.stockanalysis.StockAnalysis('aapl', '2021-03-16')


pdb.set_trace()


if __name__ == "__main__":
    app.run(debug=True)
