FROM python:3.10

### 1. Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DOCKERIZE_VERSION v0.6.1


RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN mkdir /code
COPY . /code/
WORKDIR /code

RUN set -e; \
    /usr/local/bin/python -m pip install --upgrade pip ;\
    python -m pip install --default-timeout=100 -r /code/requirements/dev.txt ;

EXPOSE 8000