
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ddebstuti:PfVbLnzuSC78xOGM@home-remedies.ahydxns.mongodb.net/?retryWrites=true&w=majority&appName=home-remedies"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


disease_db=client['disease']

disease_collection=disease_db.disease_demo


def fetch_from_db(query: dict):
    return disease_collection.find(query)


def insert_in_db(record: dict):
    disease_collection.insert_one(record)

