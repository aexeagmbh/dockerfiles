FROM elasticsearch
MAINTAINER Aexea Carpentry

ADD elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
RUN plugin install elasticsearch/elasticsearch-cloud-aws/2.6.0
RUN plugin install org.codelibs/elasticsearch-dataformat/1.6.0
