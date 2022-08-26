#!/bin/bash
docker build --tag python-docker .
docker run --name flask-auth-api -d -p 5478:5000 python-docker