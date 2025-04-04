#!/bin/bash
echo "Running collectstatic..."
source /var/app/venv/*/bin/activate
python3 manage.py collectstatic --noinput
