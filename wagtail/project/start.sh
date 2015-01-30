#!/bin/sh

sleep 5

python3 manage.py migrate --noinput
python3 manage.py runscript create_admin
# python3 manage.py runserver 0.0.0.0:8000
gunicorn project.wsgi:application --log-level=debug --log-file=/log/gunicorn.log -b 0.0.0.0:8000
