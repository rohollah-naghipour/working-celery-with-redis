from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length= 150, null = False, unique= True)
    password = models.CharField(max_length = 15, unique = True, null = False)
    email = models.EmailField(max_length= 250)
