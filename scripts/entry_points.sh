#!/usr/bin/env bash

set -e

RUN_MANAGE_PY='python -m manage.py'

echo 'Collecting static files...'
$RUN_MANAGE_PY collectstatic --no-input

echo 'Running migrations...'
$RUN_MANAGE_PY migrate --no-input

exec python -m daphne core.asgi:application -p 8000 -b 0.0.0.0
