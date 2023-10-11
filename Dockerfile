FROM ubuntu:latest

RUN apt update && apt install -y python3.10 python3-pip

RUN mkdir /app
WORKDIR /app

COPY . /app
