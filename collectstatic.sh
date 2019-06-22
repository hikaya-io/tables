#!/usr/bin/env sh

# All this environment variables need to be defined to run collectstatic
export ALLOWED_HOSTS=nothing
export CORS_ORIGIN_WHITELIST=nothing
export DJANGO_SETTINGS_MODULE=hikaya.settings.local

python manage.py collectstatic --no-input
