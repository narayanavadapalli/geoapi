cd /code/geoapi
python manage.py jsonpoller & #>> /logs/poller.log & 
python manage.py countrydetecter #>> /logs/countries.log ;