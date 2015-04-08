FROM ubuntu:14.04
MAINTAINER Aexea Carpentry

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install flower

ENTRYPOINT ["celery", "flower"]
