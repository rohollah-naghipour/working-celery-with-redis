
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


app = Celery('core')

app.config_from_object('django.conf:setting', namespace= 'CELERY')




#app.autodiscover_tasks()



