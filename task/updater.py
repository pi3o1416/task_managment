
from apscheduler.schedulers.background import BackgroundScheduler
from .update_notification import push_notification

def start():
    push_notification()
    scheduler = BackgroundScheduler()
    scheduler.add_job(push_notification, 'interval', hours=1)
    scheduler.start()

