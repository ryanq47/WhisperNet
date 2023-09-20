FROM ubuntu:latest
RUN apt-get update &&\
    apt-get install python3 -y
 
RUN apt-get install python3-pip -y
RUN python3 -m pip install Flask flask-jwt-extended requests pyyaml waitress
 
RUN mkdir /listener
COPY . /listener
 
EXPOSE 8888
CMD ["/usr/bin/python3", "/listener/FlaskAPI.py", "--ip", "0.0.0.0", "--port", "8888"]
 
## Run me with: 
## sudo docker run -d -p 8888:8888 listener:v1 
