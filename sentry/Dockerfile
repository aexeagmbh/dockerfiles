FROM aexea/aexea-base
MAINTAINER Aexea Carpentry

RUN apt-get update && apt-get install -y python-pip python-dev
RUN pip install sentry[postgres]

ADD start.sh /start.sh
RUN chmod +x /start.sh
ADD sentry.conf.py /etc/sentry.conf.py
EXPOSE 9000

ENTRYPOINT ["start.sh"]
CMD web
