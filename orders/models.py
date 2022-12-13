from django.db import models
from products.models import Products
choices = (
    ('Pending', 'Pending'),
    ('Packed', 'Packed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered')
)
# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE ,
     related_name='pro_order', blank=False, null=False)
    address = models.CharField(max_length=150, blank=False, null=False)
    pin_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        choices=choices, max_length=10, default='Pending')
    total_price = models.FloatField(null=False, blank=False)
    phone = models.CharField(max_length=100, null=True, blank=False)
    class Meta:
        ordering = ('-created', 'id', )

    def __str__(self):
        return self.address
