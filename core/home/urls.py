from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='Home'),
    path('test/', views.test, name = 'Test'),
]


