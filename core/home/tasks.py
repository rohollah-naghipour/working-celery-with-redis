
from django.core.mail import send_mail
from .models import User

from core.celery import app 
from celery import shared_task

import time

@shared_task
def send_email_to_all_users(subject, message):
    emails = User.objects.values_list('email', flat=True)
    #users = User.objects.all()  
    #emails = [user.email for user in users if user.email]
    if emails:
        send_mail(subject,message,'from@example.com',emails, fail_silently=True)
                 

@app.task
def my_task():
    time.sleep(10)
    open('test.txt', 'w').close()
