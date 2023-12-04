
import os

from django.core.wsgi import get_wsgi_application
from apscheduler.schedulers.background import BackgroundScheduler

from mailings.apscheduler import job_function

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job_function,  'interval', minutes=3)
    scheduler.start()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
start_scheduler()
