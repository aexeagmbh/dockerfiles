FROM elasticsearch
MAINTAINER Aexea Carpentry

ADD elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
RUN apt-get install -y wget unzip
RUN mkdir -p /opt/elasticsearch/plugins/cloud-aws
WORKDIR /opt/elasticsearch/plugins/cloud-aws
RUN wget http://download.elasticsearch.org/elasticsearch/elasticsearch-cloud-aws/elasticsearch-cloud-aws-2.6.0.zip
RUN unzip elasticsearch-cloud-aws-2.6.0.zip

# RUN plugin install elasticsearch/elasticsearch-cloud-aws/2.6.0
