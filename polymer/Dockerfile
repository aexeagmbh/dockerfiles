FROM ubuntu:14.04
MAINTAINER Aexea Carpentry

RUN apt-get update && apt-get install -y \
    curl \
    && apt-get clean
RUN curl -sL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y \
    xvfb
    firefox
    google-chrome-stable \
    nodejs \
    nodejs-legacy \
    npm \
    git \
    default-jre \
    ruby \
    ruby-dev \
    build-essential \
    && apt-get clean

RUN gem install sass
RUN gem install sass-css-importer --pre
RUN npm install -g bower gulp generator-polymer

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN useradd uid1000 -d /home/uid1000
RUN mkdir -p /home/uid1000 && chown uid1000: /home/uid1000
VOLUME /home/uid1000

RUN mkdir -p /opt/code
RUN chown uid1000:uid1000 /opt/code
WORKDIR /opt/code
USER uid1000
