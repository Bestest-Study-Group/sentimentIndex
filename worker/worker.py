import os
import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv('REDISTOGO_URL', 'redis://my-redis:6379')


conn = redis.from_url(redis_url)

if __name__ == '__main__':
    print("GGGGGGG")
    print(redis_url)
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()