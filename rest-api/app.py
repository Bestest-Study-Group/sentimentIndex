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

app = Flask("MYAPP")
CORS(app)


@app.route("/api/reddit")
def hello_world():
    colleciton = db.test
    results = list(colleciton.find({}))
    # convert OjectID to string
    for res in results:
        res['_id'] = str(res['_id'])
    print(results)
    return {"data":results}

@app.route("/api/news")
def hello_world():
    colleciton = db.test
    results = list(colleciton.find({}))
    # convert OjectID to string
    for res in results:
        res['_id'] = str(res['_id'])
    print(results)
    return {"data":results}