import os
import redis
from rq import Worker, Queue, Connection

# from sentiment_analyser.individual_classification import IndividualClassification

listen = ['high', 'default', 'low']

redis_url = os.getenv('REDISTOGO_URL', 'redis://my-redis:6379')
print(redis_url)


conn = redis.from_url(redis_url)

if __name__ == '__main__':
    print(redis_url)
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()