FROM python:3.5

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install vim -y
RUN apt-get install curl -y
RUN curl http://j.mp/spf13-vim3 -L -o - | sh
 
ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install --no-cache-dir -r requirements.txt

ONBUILD COPY . /usr/src/app
