FROM python:3.7-stretch

RUN pip install "devpi-server<4.10" "devpi-web<3.6"

RUN mkdir /devpi
WORKDIR /devpi

EXPOSE 3141

ENTRYPOINT "devpi-server"
CMD "--start"
