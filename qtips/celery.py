import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qtips.settings')

app = Celery('qtips')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
    'send-balance-info': {
        'task': 'api.tasks.send_balance_info',
        'schedule': crontab(minute=0, hour=0),
    },
}
