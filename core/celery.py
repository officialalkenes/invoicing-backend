from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

app.conf.enable_utc = False
app.conf.update(timezone="Africa/Lagos")

# # Using a string here means the worker will not have to
# # pickle the object when using Windows.
# app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object(settings, namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# CELERY_BEAT_SETTINGS
app.conf.beat_schedule = {
    "fetch-banks-every-12-hours": {
        "task": "your_app.tasks.fetch_and_store_banks",
        "schedule": crontab(hour="*/12"),
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f"Request {self.request!r}")
