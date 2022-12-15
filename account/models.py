from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser

class Account (AbstractBaseUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email