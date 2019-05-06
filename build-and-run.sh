#!/usr/bin/env bash
image_name="grpc-python-message-to-dict"
echo Building image...
docker build -q -t ${image_name} .
echo Running container...
docker run --rm ${image_name}
echo Done!
