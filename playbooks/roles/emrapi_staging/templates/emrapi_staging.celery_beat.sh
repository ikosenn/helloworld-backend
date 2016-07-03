#!/usr/bin/env bash

cd {{install_dir}}
source {{venv_dir}}/bin/activate && source {{install_dir}}/env.sh && exec celery -A emrapp.config  beat --loglevel=INFO --pidfile=/tmp/celerybeat-emr.pid --schedule={{install_dir}}/celerybeatemr-schedule
