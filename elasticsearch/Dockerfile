FROM elasticsearch
MAINTAINER Aexea Carpentry

RUN mkdir -p /opt/elasticsearch/plugins
RUN chmod -R 777 /opt
ADD elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
RUN plugin install elasticsearch/elasticsearch-cloud-aws/2.4.1
