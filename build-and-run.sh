#!/usr/bin/env bash
docker rm -f gpm2d-client gpm2d-server

docker network create grpc-python-message-to-dict

docker build -q -t grpc-python-message-to-dict .

common_command="docker run -d --network grpc-python-message-to-dict"
${common_command} --name gpm2d-server grpc-python-message-to-dict
${common_command} --name gpm2d-client grpc-python-message-to-dict client.py
CLIENT_PID=$?
wait ${CLIENT_PID}

docker logs -t gpm2d-server
echo ''
docker logs -t gpm2d-client
