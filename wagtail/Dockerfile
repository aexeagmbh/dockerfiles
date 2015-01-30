FROM aexea/aexea-base
MAINTAINER Aexea Carpentry

RUN apt-get install g++
RUN pip3 install wagtail

ADD project/requirements.txt /opt/code/requirements.txt
WORKDIR /opt/code
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn django-extensions

ADD project /opt/code

RUN chown -R uid1000: .
RUN chmod +x start.sh
RUN mkdir /log
RUN chown -R uid1000: /log

EXPOSE 8000
USER uid1000

ENTRYPOINT ./start.sh
CMD web
