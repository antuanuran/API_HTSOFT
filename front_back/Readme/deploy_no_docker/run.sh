#!/usr/bin/env bash

set -euxo pipefail

pip3 install -r requirements.txt
python3 manage.py collectstatic --no-input
python3 manage.py migrate --no-input
gunicorn frontend_gstreamer.wsgi --bind 127.0.0.1:8000 --workers 4 --timeout 6000
