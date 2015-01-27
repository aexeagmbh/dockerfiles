FROM aexea/aexea-base
MAINTAINER Aexea Carpentry

RUN apt-get update && apt-get install -y python-pip python-dev
RUN pip install sentry sentry[postgres]

ADD sentry.conf /etc/sentry.conf.py
EXPOSE 9000

CMD sentry --config=/etc/sentry.conf.py celery worker -B
