#!/usr/bin/env bash
docker rm -f client server

docker network create intercept

docker build -t intercept .

docker run -d --name server --network intercept intercept
docker run -d --name client --network intercept intercept client.py

docker logs -t server
echo ''
docker logs -t client
