from django.http import HttpResponse
from django.shortcuts import render
from core.celery import app 
import time

@app.task
def my_task():
    time.sleep(10)
    open('test.txt', 'w').close()


def home(request):
    my_task()
    return HttpResponse("welcome to Home page")


