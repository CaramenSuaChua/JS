from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=100, null=True, blank=True, related_name='name')
#     first_name = models.CharField(max_length=100, related_name='ten')
#     last_name = models.CharField(max_length=100, related_name='ho')
#     email = models.EmailField(max_length=100, unique=True, related_name='email')
#     is_staff = models.BooleanField(default=False, related_name='check_staff')

#     USERNAME_FIELD = ['email', ]
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.email
    