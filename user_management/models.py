from django.db import models
from django.contrib.auth.models import AbstractUser
from core.managers import CustomUserManager


class CustomUser(AbstractUser):    
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    address = models.TextField()
    phone_number = models.CharField(max_length=10)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()