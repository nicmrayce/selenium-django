release: python manage.py migrate --noinput
web gunicorn --timeout 300 main.wsgi:application --log-file -