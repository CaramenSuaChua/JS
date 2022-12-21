from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
class UserModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True,blank=True)
    last_name = models.CharField(max_length=150, null=True,blank=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username