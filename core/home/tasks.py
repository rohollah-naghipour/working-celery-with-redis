
from celery import shared_task

from home.models import User
from core.celery import app 

from django.core.mail import EmailMessage

import time


@shared_task
def send_email_to_all_users(subject, message):
    emails = User.objects.values_list('email', flat=True)
    #users = User.objects.all()  
    #emails = [user.email for user in users if user.email]
    if emails:
        email = EmailMessage(subject,
                             message,
                             'alitezanaghipour@gmail.com',
                             emails,
                             fail_silently=True)
        email.send() 

@app.task
def my_task():
    time.sleep(10)
    open('test.txt', 'w').close()
