from django.contrib import admin

#import models
from .models import Delivery, DeliveryUnit
# Register your models here.
admin.site.register(Delivery)
admin.site.register(DeliveryUnit)