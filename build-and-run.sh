#!/usr/bin/env bash
image_name="grpc-python-message-to-dict"
docker build -q -t ${image_name} .
docker run --rm ${image_name}
