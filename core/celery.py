import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.worker_state_db = "/tmp/celery-worker.state"
# app.conf.beat_schedule_filename = "/tmp/celerybeat-schedule"