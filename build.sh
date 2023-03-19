#!/bin/bash

# Build the project
echo "Building the project..."
pip install --upgrade pip
python -m pip install -r requirements.txt

echo "Make Migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect Static..."
python manage.py collectstatic --noinput --clear
