# syntax=docker/dockerfile:1
# Base Image will be python 3.7 alpine image
FROM python:3.7-alpine
#CMD ["echo", "Building Broker Image"]
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
#CMD ["python", "brokerapp/pullJson.py"]