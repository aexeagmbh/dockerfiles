FROM aexea/aexea-base
MAINTAINER Aexea Carpentry

ONBUILD ADD requirements.txt /opt/code/requirements.txt
ONBUILD WORKDIR /opt/code
ONBUILD RUN pip3 install -Ur requirements.txt

ONBUILD ADD . /opt/code
ONBUILD WORKDIR /opt/code
ONBUILD USER uid1000
