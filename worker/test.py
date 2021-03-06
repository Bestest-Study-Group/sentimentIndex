# this is just to test if worker and redis are working
from rq import Queue
from rq.job import Job
import time
from pymongo import MongoClient
from random import randint
from dotenv import load_dotenv
import redis
import os

load_dotenv()
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASS = os.getenv('MONGO_PASS')

client = MongoClient(f'mongodb+srv://{MONGO_USER}:{MONGO_PASS}@cluster0.tk2cy.mongodb.net/?retryWrites=true&w=majority')
redis_url = os.getenv('REDISTOGO_URL', 'redis://my-redis:6379')
print(redis_url)
conn = redis.from_url(redis_url)

q = Queue(connection=conn)
# foldername.filename.functionname
reddit = 'sentiment_analyser.redditsenti.run'
news ='sentiment_analyser.newssenti.run'

def wait_for_job(function_to_call):
    job = q.enqueue(function_to_call)
    finished = False
    while not finished:
        time.sleep(1)
        fetched_job = Job.fetch(job.id, conn)
        finished = fetched_job.is_finished
        if finished:
            print(f'{function_to_call} with jobId {fetched_job.id} finished with following result:\n {fetched_job.result}')
            # Store result in MongoDB
            db=client.run1

            data = {
                "functionCalled":function_to_call,
                "jobId":fetched_job.id,
                "result":fetched_job.result
            }
            res = {}
            if (function_to_call == reddit):
                res = db['reddit'].insert_one({'chart_data': fetched_job.result})
            elif (function_to_call == news):
                res = db['news'].insert_one({'chart_data': fetched_job.result})

            print(res)

            result = db.test.insert_one(data)
            print(result)

wait_for_job(reddit)
wait_for_job(news)

