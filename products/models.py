from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.name

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,\
    related_name='cate_pro', null=False, blank=False)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    availibility = models.BooleanField(default=True, null=False)
    # image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    
    class Meta:
        ordering = ('id', )
    def __str__(self):
        return self.name