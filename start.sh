#!/bin/bash
ps -aux | grep 8003 | awk '{print $2}' | xargs kill -9
gunicorn TelephoneCard.wsgi.application -b 0.0.0.0:8003 -w 4 -t 300 --reload
