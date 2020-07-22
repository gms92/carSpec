from pymongo import MongoClient
import pprint
import os

client = MongoClient(os.environ.get('MONGO_URL'))

db = client.get_database('test')

def saveToMongo(carSpec):
    db.spec.insert(carSpec)




