from django.http import HttpResponse
from django.shortcuts import render
from .tasks import my_task
from .models import User


def home(request):
    my_task.delay()
    return HttpResponse("welcome to Home page")

def test(request):
    user_details = User.objects.values('username', 'email')
    #emails = User.objects.values_list('email', flat=True)
    #print(emails)
    print(user_details)
    return HttpResponse("for test API")

