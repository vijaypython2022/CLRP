import os
import django
from django.conf import settings
from celery import Celery

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CLRP.settings')
django.setup()
# Initialize the Celery app
app = Celery('CLRP')
app.config_from_object('django.conf:settings')

# Load Django settings
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Import and execute the task
from Api.tasks import expire_reward_points_task

expire_reward_points_task.delay()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
