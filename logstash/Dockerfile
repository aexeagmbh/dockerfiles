FROM java:7-jre
MAINTAINER Aexea Carpentry

# Download version 1.4.2 of logstash
RUN cd /tmp && \
    wget https://download.elastic.co/logstash/logstash/logstash-2.1.1.tar.gz && \
    tar -xzvf ./logstash-2.1.1.tar.gz && \
    mv ./logstash-2.1.1 /opt/logstash && \
    rm ./logstash-2.1.1.tar.gz

WORKDIR /opt/logstash
RUN bin/plugin install logstash-input-udp
RUN bin/plugin install logstash-input-syslog
RUN bin/plugin install logstash-filter-json
RUN bin/plugin install logstash-output-elasticsearch
RUN bin/plugin install logstash-output-amazon_es

RUN mkdir -p /conf
ADD default.conf /conf/default.conf

VOLUME /conf

CMD bin/logstash -f /conf
