# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import os

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "course.conf.stage")
app = Celery("course")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
