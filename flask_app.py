from algos import Algos
from flask import Flask

app = Flask(__name__)
# Home Page
@app.route("/")
def home():
    return "Welcome to LeetTrainer!"

# Two Sum Page
@app.route("/two_sum")
def two_sum_page():
    return "Two Sum Page"

# Buy Stocks Page
@app.route("/buy_stocks")
def buy_stock_page():
    return "Buy Stocks Page"

# Top K Page
@app.route("/top_k")
def top_k_page():
    return "Top K Page"

# Testing algo import
@app.route("/test_buy_stocks")
def test_buy_stock_page():
    algos = Algos()
    
    prices = [7, 1, 2, 3, 4, 5, 6]
    result = algos.buy_stonks(prices)
    
    return f"Maximum Profit To Be Made = ${result}"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)