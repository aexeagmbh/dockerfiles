FROM dockerfile/elasticsearch
MAINTAINER Aexea Carpentry

ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml
RUN /elasticsearch/bin/plugin install elasticsearch/elasticsearch-cloud-aws/2.4.1
