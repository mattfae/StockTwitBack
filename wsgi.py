from stocktwit import create_app
import stocktwit
import pdb


app = create_app()

print("creating new")
new = stocktwit.stockanalysis.StockAnalysis('aapl', '2021-03-16')
print("running get tweets")
new.get_tweets()
print("running analyze tweets")
new.analyze_tweets()
print("running get market data")
new.get_market_data()


pdb.set_trace()


if __name__ == "__main__":
    app.run(debug=True)
