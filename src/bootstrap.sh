#! /bin/bash

# Bootstrap database
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata urls
python manage.py loaddata user
