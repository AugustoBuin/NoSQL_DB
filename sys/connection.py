from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# import funcs from funcs.py

uri = "mongodb+srv://admin:admin@cluster0.x4apknn.mongodb.net/?retryWrites=true&w=majority"  #

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))
global db
db = client.Beelieve

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
    print(" ")
except Exception as e:
    print(e)
