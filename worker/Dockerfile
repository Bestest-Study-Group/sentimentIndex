# syntax=docker/dockerfile:1
FROM python:latest
WORKDIR /
ENV REDISTOGO_URL redis://my-redis:6379
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3", "worker.py" ]