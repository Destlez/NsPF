import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsportal_finaly.settings')

app = Celery('newsportal_finaly')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.timezone = 'UTC'