web: gunicorn qtips.wsgi --log-file -
worker: celery -A qtips worker
beat: celery -A qtips beat -S django