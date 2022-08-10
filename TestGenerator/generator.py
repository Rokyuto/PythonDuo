from bson.json_util import dumps
from pymongo import MongoClient
import json

#client = MongoClient("mongodb+srv://pyduo:pyduo@pyd.cjtsbfb.mongodb.net/?retryWrites=true&w=majority")
#db = client["pyduo"]
#collection = db["setup"]


client = MongoClient("mongodb+srv://pyduo:pyduo@pyd.cjtsbfb.mongodb.net/?retryWrites=true&w=majority")
db = client["pyduo"]
collection = db["setup"]
cursor = collection.find({})
with open('collection.json', 'w') as file:
    for document in cursor:
        file.write(dumps(document))
        file.write(',')

        