
from home.tasks import my_task
from home.models import User
from home.tasks import send_email_to_all_users

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    my_task.delay()
    return HttpResponse("welcome to Home page")


def send_email(request):
    subject = "send email for all user"
    message = "this message is for test........:)"
    send_email_to_all_users.apply_async(args=[subject, message])
    return HttpResponse("**********send_email**********")



def test(request):
    user_details = User.objects.values('username', 'email')
    #emails = User.objects.values_list('email', flat=True)
    #print(emails)
    print(user_details)
    return HttpResponse("for test API")

