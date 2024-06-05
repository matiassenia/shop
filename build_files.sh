#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Create a directory for the static files
#mkdir -p staticfiles_build
#cp -r staticfiles/* staticfiles_build/