from django.db import models
from products.models import Products
# Create your models here.
class DeliveryUnit(models.Model):
    name= models.CharField(max_length=200,null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return str(self.name)


class Delivery(models.Model):
    products = models.ManyToManyField(Products, related_name='deli')
    deliveryUnit = models.ForeignKey(DeliveryUnit, null=True, blank=True, related_name='delivery',on_delete=models.SET_NULL)
    startdate = models.DateField("startdate", auto_now=False, auto_now_add=False)
    address = models.TextField(null=True, blank=True)
    def __str__(self):
        return str(self.address)