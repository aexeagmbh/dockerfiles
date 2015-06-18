FROM elasticsearch
MAINTAINER Aexea Carpentry

RUN mkdir -p /opt/elasticsearch/plugins
ADD elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
RUN plugin install elasticsearch/elasticsearch-cloud-aws/2.6.0
