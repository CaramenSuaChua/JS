from django.db import models
from products.models import Products
from django.contrib.auth.models import User
choices = (
    ('Pending', 'Pending'),
    ('Packed', 'Packed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered')
)

class OrderItem(models.Model):
    product = models.ManyToManyField(Products, 
      related_name="orders")
    quantity = models.PositiveIntegerField(default=1)
    total = models.FloatField(null=False, blank=False)
    
    def __str__(self):
        return str(self.id)

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user')
    order_item = models.ManyToManyField(OrderItem, verbose_name="items",blank=False, null=False)
    address = models.CharField(max_length=150, blank=True, null=True)
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
        return str(self.id)

