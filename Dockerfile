FROM python:3.7
LABEL maintainer="sergey.nevmerzhitsky@gmail.com"

COPY docker-main.sh /docker/

WORKDIR /var/app/src

COPY requirements.txt .
RUN set -ex; \
    pip install --upgrade pip; \
    pip install --no-cache-dir -r requirements.txt

COPY src/ .

RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. test.proto

CMD ["bash", "/docker/docker-main.sh"]
