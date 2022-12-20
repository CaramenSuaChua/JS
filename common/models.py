from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
    username = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True,blank=True)
    last_name = models.CharField(max_length=150, null=True,blank=True)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    is_active = models.BooleanField(default=True,null=True,blank=True)
    is_staff = models.BooleanField(default=False,null=True,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']