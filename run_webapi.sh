#!/bin/sh

# wait for PSQL server to start
sleep 10

su -m root -c "python manage.py makemigrations"
su -m root -c "python manage.py migrate"

sleep 5
su -m root -c "python manage.py runserver 0.0.0.0:8000"