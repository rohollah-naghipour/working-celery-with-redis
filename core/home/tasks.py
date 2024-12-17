from core.celery import app 
import time

@app.task
def my_task():
    time.sleep(10)
    open('test.txt', 'w').close()
