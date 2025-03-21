from flask import Flask, jsonify, request
from utils.stock_api import get_stock_data

app = Flask(__name__)

@app.route('/stock/<symbol>', methods=['GET'])
def get_stock(symbol):
    data = get_stock_data(symbol)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
