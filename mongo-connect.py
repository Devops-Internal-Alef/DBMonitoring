import sys

# Install Pymongo driver to use this
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27018")
db = client.admin
try:
    db.command("ismaster")
    print("Connection to the MongoDB Database is sucessful")
    client.close()
    sys.exit(0)
except Exception as e:
    print("Connection to MongoDB failed", e)
    sys.exit(2)
