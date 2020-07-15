from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)

db = client.get_database('techtop')

def saveToMongo(carSpec):
    db.carSpec.insert(carSpec)




