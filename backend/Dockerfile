# syntax=docker/dockerfile:1
# Base Image will be python 3.7 alpine image
FROM python:3.8.12-slim-buster
#CMD ["echo", "Building Broker Image"]
WORKDIR /code

RUN apt-get update && apt-get install -y \
    libpq-dev \
    binutils libproj-dev gdal-bin proj-bin libgeos++

#COPY requirements.txt requirements.txt
COPY . .
RUN pip install -r requirements.txt

#  ["python","manage.py migrate"]
#CMD ["python", "brokerapp/pullJson.py"]