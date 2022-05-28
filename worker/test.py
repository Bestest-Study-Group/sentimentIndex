# this is just to test if worker and redis are working
from rq import Queue
from rq.job import Job
from worker import conn
import time
from pymongo import MongoClient
from random import randint
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASS = os.getenv('MONGO_PASS')

client = MongoClient(f'mongodb+srv://{MONGO_USER}:{MONGO_PASS}@cluster0.tk2cy.mongodb.net/?retryWrites=true&w=majority')

db=client.run1
result = db.test.insert_one({"testNum":randint(1, 10000)})
print(result)


q = Queue(connection=conn)
# foldername.filename.functionname
job = q.enqueue("sentiment_analyser.utils.count_words_at_url", 'http://heroku.com')
finished = False
while not finished:
    time.sleep(1)
    fetched_job = Job.fetch(job.id, conn)
    finished = fetched_job.is_finished
    if finished:
        print(f'Job {fetched_job.id} finished with following result:\n {job.result}')
