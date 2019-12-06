import os

from celery import Celery
from celery.schedules import crontab

from . import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shortener.settings')

app = Celery('shortener')
app.config_from_object(config)

app.autodiscover_tasks(packages=['shortener.apps.link', 'shortener.apps.analytics', ])

app.conf.beat_schedule = {
    'run-every-hour': {
        'task': 'shortener.apps.analytics.tasks.runner',
        'schedule': crontab(minute=0, hour='*/1')
    },
}