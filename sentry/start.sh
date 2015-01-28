#!/bin/sh

sentry --config=/etc/sentry.conf.py upgrade

if [ "$1" -eq 'worker' ]; then
    sentry --config=/etc/sentry.conf.py celery worker -B
else
    sentry --config=/etc/sentry.conf.py start
fi
