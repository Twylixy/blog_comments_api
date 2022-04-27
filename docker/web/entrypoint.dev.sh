#!/bin/sh

# Collect database migrations
echo "Collect database migrations"
python3 ./app/manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python3 ./app/manage.py migrate

# Collect static files
echo "Collect static files"
python3 ./app/manage.py collectstatic --noinput

# Start server
echo "Starting server"
python3 ./app/manage.py runserver 0.0.0.0:8000

exec "$@"