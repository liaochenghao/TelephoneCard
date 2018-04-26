#!/bin/bash
ps -aux | grep 8001 | awk '{print $2}' | xargs kill -9
gunicorn TelephoneCard.wsgi:application -b 0.0.0.0:8001 -w 4 -t 300 --reload
