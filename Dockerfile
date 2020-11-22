FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
MAINTAINER TelegramBot


RUN apt-get update -y \
&& apt-get upgrade -y \
&& apt-get install -y apt-utils \
&& apt-get install gcc -y \
&& apt-get clean \
&& apt-get install -y python3-setuptools \
&& apt-get install -y rabbitmq-server \
&& apt-get install -y systemd \
&& apt-get install -y build-essential python-dev libffi-dev \
&& python3 -m pip install --upgrade pip




COPY Bot/requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt


RUN mkdir /TelegramBot
WORKDIR /TelegramBot
COPY ./Bot ./TelegramBot
