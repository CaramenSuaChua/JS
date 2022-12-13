from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=1000, null=True, blank=True)
    
    class Meta:
        ordering = ('id', )
    def __str__(self):
        return self.name