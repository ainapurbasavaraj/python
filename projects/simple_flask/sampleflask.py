from crypt import methods
from flask import Flask, jsonify, request
from flask_restful import Resource

import json

app = Flask(__name__)

stores = [
    {
        'name': 'my_store',
        'items': [
            {
                'name': 'my_item',
                'price': 15.99
            }
        ]
    }
]

#BElow are the endopoints

# POST /store data: {name:}
@app.route("/store", methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name']
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/name
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if name == store.get("name"):
            return jsonify(store)
    return "None"

# GET /store
@app.route("/stores")
def get_stores():
    return jsonify({'stores': stores})

#POST /store/<string:name>/item {name:, price:,}
@app.route("/store/<string:name>/item", methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if name == store.get('name'):
            store['items'] = []
            new_item = {
                'name' : request_data['name'],
                'price' : request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return "None"            

# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if name == store.get("name"):
            return jsonify({'items': store.get("items")})
    return "None"

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5000)
