from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASS = os.getenv('MONGO_PASS')
client = MongoClient(f'mongodb+srv://{MONGO_USER}:{MONGO_PASS}@cluster0.tk2cy.mongodb.net/?retryWrites=true&w=majority')
db=client.run1

app = Flask(__name__)
CORS(app)


@app.route("/api/reddit")
def reddit():
    collection = db.reddit_individual
    results = list(collection.find({}))
    # convert OjectID to string
    for res in results:
        res['_id'] = str(res['_id'])
    print(results)
    return {"data":results}

@app.route("/api/news")
def news():
    collection = db.test
    results = list(collection.find({}))
    # convert OjectID to string
    for res in results:
        res['_id'] = str(res['_id'])
    print(results)
    return {"data":results}