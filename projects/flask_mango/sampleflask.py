from crypt import methods
from flask import Flask, jsonify, request
from flask_restful import Resource
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib.parse
import json

'''
Mongodb connection string
mongodb+srv://<username>:<password>@basavaraj-cluster.8gchilj.mongodb.net/?retryWrites=true&w=majority
'''
username = urllib.parse.quote_plus('bainapur')
password = urllib.parse.quote_plus('Amadeus@125')
uri = 'mongodb+srv://%s:%s@basavaraj-cluster.8gchilj.mongodb.net/?retryWrites=true&w=majority' %(username,password)
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["my_store-db"]
collection = db.my_store

app = Flask(__name__)


#BElow are the endopoints

# POST /store data: {name:}
@app.route("/store", methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = [{
        "name" : request_data["name"]
    }]
    result = collection.insert_many(new_store)
    print(result.inserted_ids)
    return jsonify(str(new_store))

# GET /store/name
@app.route("/store/<string:name>")
def get_store(name):
    return jsonify(str(collection.find_one({"name": name})))

# GET /store
@app.route("/stores")
def get_stores():
    stores = []
    for x in collection.find({}):
        stores.append(x)
    
    return jsonify(str(stores))

#POST /store/<string:name>/item {name:, price:,}
@app.route("/store/<string:name>/item", methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    query = {"name" : name}
    newValues = {"$set" : {
        "name" : name,
        "items" : [
            {
                "name" : request_data["name"],
                "price" : request_data["price"]
            }
        ]
    }}
    collection.update_one(query,newValues)
    
    updated_list = [x for x in collection.find({})]
    return jsonify(str(updated_list))

# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    store = collection.find_one({"name": name})
    return jsonify({'items': store.get("items")})
    

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5000)
