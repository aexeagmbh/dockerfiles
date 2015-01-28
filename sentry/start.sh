#!/bin/sh

echo "Starting sentry $1"
sentry --config=/etc/sentry.conf.py upgrade

if [ "$1" -eq 'worker' ]; then
    sentry --config=/etc/sentry.conf.py celery worker -B
else
    sentry --config=/etc/sentry.conf.py start
fi
