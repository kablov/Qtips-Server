import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qtips.settings')

app = Celery('qtips')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    'send-balance-info': {
        'task': 'api.tasks.send_balance_info',
        'schedule': 30,  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}
