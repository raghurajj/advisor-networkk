release: pyhton manage.py makemigrations --no-input
release: pyhton manage.py migrate --no-input

web: gunicorn rest.wsgi --log-file -