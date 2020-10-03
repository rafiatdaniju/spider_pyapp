from celery import Celery
from src.spider import fetch_record
from decouple import config
from src.db import DB

# me= DB()
# # me.connect()
# # me.setup()
# me.seed()

app = Celery('crawler', backend=config('CELERY_BACKEND'), broker=config('CELERY_BROKER'), CELERY_IGNORE=config('CELERY_IGNORE'),
CELERY_TRACK_STARTER = config('CELERY_TRACK_STARTER'))

@app.task()
def foo_task(id):
    return fetch_record(id)

# fetch_record(2)

    
    