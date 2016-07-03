#!/usr/bin/env bash
export SECRET_KEY="{{emrapi_secret_key}}"
export DEBUG="false"
export SIL_EMR_DATABASE_URL="{{database_url}}"
export EMRAPP_PORT="{{emrapi_staging_port}}"
export CSRF_COOKIE_NAME="{{csrf_cookie_name}}"
export SESSION_COOKIE_NAME="{{session_cookie_name}}"
export STATIC_ROOT="{{static_dir}}"
export MEDIA_ROOT="{{media_dir}}"
export HOST="{{server_domain}}"
export SIL_EMR_LIBCLOUD_STORAGE="{{libcloud_storage}}"
export SIL_EMR_LIBCLOUD_PROVIDER="{{libcloud_provider}}"
export SIL_EMR_LIBCLOUD_TYPE="{{libcloud_type}}"
export SIL_EMR_LIBCLOUD_USER="{{libcloud_user}}"
export SIL_EMR_LIBCLOUD_KEY="{{libcloud_key}}"
export SIL_EMR_LIBCLOUD_BUCKET="{{libcloud_bucket}}"
export VENV_DIR="{{venv_dir}}"
export EMR_AWS_KEY_ID="{{aws_key_id}}"
export EMR_AWS_SECRET="{{aws_secret}}"
export EMR_FRONTEND_URL="{{front_end_url}}"
export EMR_BACKEND_URL="{{server_domain}}"
export HTTPS_ENABLED="{{ssl_on}}"
# a hack for python 3 and boto
# https://github.com/travis-ci/travis-ci/issues/5246
export BOTO_CONFIG="/tmp/bogus"