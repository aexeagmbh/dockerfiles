FROM aexea/aexea-base
MAINTAINER Aexea Carpentry

RUN apt-get update && apt-get install -y python-pip python-dev
RUN pip install sentry[postgres]

ADD start.sh /usr/bin/local/start
RUN chmod +x /usr/bin/local/start
ADD sentry.conf.py /etc/sentry.conf.py
EXPOSE 9000

CMD /start.sh web
