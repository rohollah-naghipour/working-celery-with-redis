from django.http import HttpResponse
from django.shortcuts import render
from .tasks import my_task



def home(request):
    my_task.delay()
    return HttpResponse("welcome to Home page")


