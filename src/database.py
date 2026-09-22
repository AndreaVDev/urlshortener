from pymongo import AsyncMongoClient
# Mongo connection setup

client = AsyncMongoClient("mongodb://localhost:27017/")
db = client["url_shortener"]
urls_collection = db["urls"]