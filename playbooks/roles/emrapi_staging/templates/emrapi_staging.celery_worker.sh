#!/usr/bin/env bash

cd {{install_dir}}
source {{venv_dir}}/bin/activate && source {{install_dir}}/env.sh && exec celery worker -A emrapp.config --loglevel=INFO
