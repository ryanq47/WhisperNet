FROM ubuntu:latest
RUN apt-get update &&\
    apt-get install python

RUN mkdir /listener
COPY . /listener

CMD ["/usr/bin/python3", "/listener/FlaskAPI.py", "--ip 0.0.0.0", "--port 8080"]
