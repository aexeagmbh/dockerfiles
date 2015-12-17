FROM java:7-jre
MAINTAINER Aexea Carpentry

# Download version 1.4.2 of logstash
RUN cd /tmp && \
    wget https://download.elasticsearch.org/logstash/logstash/logstash-1.4.2.tar.gz && \
    tar -xzvf ./logstash-1.4.2.tar.gz && \
    mv ./logstash-1.4.2 /opt/logstash && \
    rm ./logstash-1.4.2.tar.gz

WORKDIR /opt/logstash
RUN bin/plugin install contrib
RUN bin/plugin install logstash-output-amazon_es

RUN mkdir -p /conf
ADD default.conf /conf/default.conf

VOLUME /conf

CMD bin/logstash -f /conf
