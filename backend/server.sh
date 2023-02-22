cd /code/geoapi
gunicorn --timeout=1000 --bind=0.0.0.0:8000 geoapi.wsgi
#python manage.py makemigrations && python manage.py migrate;
#python manage.py runserver 0.0.0.0:8001