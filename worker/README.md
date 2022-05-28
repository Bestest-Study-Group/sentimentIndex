## INFO

It works but needs to be cleaned up. Very messy

## Setup

`cd worker`

`docker-compose up --build`

The `--build` will rebuild the images, so that any code changes you make will be reflected.

## Interactive

After docker containers are running, open another terminal

`docker exec -it worker_web_1 bash`

then run the test script to see if is working

`python3 test.py`

If you see the result of the job then its working

## Making code changes

If you make code changes and want the docker container to be updated

1. Stop the docker container (in the GUI or Control + C)
2. Remove old images `docker image prune -a`
3. `docker-compose up --build`
