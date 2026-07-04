from datetime import datetime
from algos import Algos
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from file_utils import log_history
from file_utils import load_history
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})
# Home Page
@app.route("/")
def home():
    return f"""
    <h1>LeetTrainer Landing Page</h1>
    <p>Welcome to the Leet Trainer Landing page</p>
    This application is currently under development
    """

@app.route("/api/binary-search", methods=["POST"])
def binary_search():
    data = request.get_json()
    numbers = data["numbers"]
    target = data["target"]
    algos = Algos()
    result = algos.binary_search(numbers, target)

    log_history(
        algorithm="Binary Search",
        inputs={"numbers": numbers, "target": target},
        result=result,
        timestamp=datetime.now()
    )

    return jsonify({"result": result})

@app.route("/api/two-sum", methods=["POST"])
def api_two_sum():
    data = request.get_json()
    nums = data["nums"]
    target = data["target"]
    algos = Algos()
    result = algos.two_sum(nums, target)

    log_history(
        algorithm="Two Sum",
        inputs={"nums": nums, "target": target},
        result=result,
        timestamp=datetime.now()
    )

    return jsonify({"result": result})

@app.route("/api/sliding-window", methods=["POST"])
def api_sliding_window():
    data = request.get_json()
    string_value = data["string"]
    algos = Algos()
    result = algos.sliding_window(string_value)

    return jsonify({"result": result})

@app.route("/api/top-k-frequency", methods=["POST"])
def api_top_k_frequency():
    data = request.get_json()
    numbers = data["numbers"]
    k = data["k"]
    algos = Algos()
    result = algos.top_k_frequency(numbers, k)

    log_history(
        algorithm="Top K Frequency",
        inputs={"numbers": numbers, "k": k},
        result=result,
        timestamp=datetime.now()
    )

    return jsonify({"result": result})

@app.route("/api/valid-parentheses", methods=["POST"])
def api_valid_parentheses():
    data = request.get_json()
    string_value = data["string"]
    algos = Algos()
    result = algos.valid_parenth(string_value)

    log_history(
        algorithm="Valid Parentheses",
        inputs={"string": string_value},
        result=result,
        timestamp=datetime.now()
    )

    return jsonify({"result": result})

# Two Sum Page
@app.route("/two_sum")
def two_sum_page():
    algos = Algos()
    
    nums = [1,2,3,4]
    targ = 5
    
    result = algos.two_sum(nums, targ)
    
    return f"""
    <h1>Two Sum Landing Page</h1>
    <p>Welcome to the Two Sum algorithim page</p>
    Here are the locations of combos from your arrary that are equal to {targ}: {result}
    """

# Buy Stocks Page
@app.route("/api/buy-stocks", methods=["POST"])
def api_buy_stocks():
    data = request.get_json()
    prices = data["prices"]
    algos = Algos()
    result = algos.buy_stonks(prices)

    log_history(
        algorithm="Buy Stocks",
        inputs={"prices": prices},
        result=result,
        timestamp=datetime.now()
    )
    
    return jsonify({"result": result})

@app.route("/api/history", methods=["GET"])
def api_history():
    history = load_history()
    return jsonify(history)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
    