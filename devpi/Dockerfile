FROM python:3.7

RUN pip install "devpi-server<4.7" "devpi-web<3.4"

RUN mkdir /devpi
WORKDIR /devpi

EXPOSE 3141

ENTRYPOINT "devpi-server"
CMD "--start"
