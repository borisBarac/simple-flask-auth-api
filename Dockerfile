# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /flask-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m", "flask", "--app=./api/app", "run"