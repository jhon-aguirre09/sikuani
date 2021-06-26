from flask import Flask
import pymongo

app = Flask(__name__)

@app.route('/')
def hello():
    client = pymongo.MongoClient("mongodb+srv://new_user:sikuani@cluster0.vxniy.mongodb.net/sikuanidb?retryWrites=true&w=majority") 
    db = client.test
    return str(db)
