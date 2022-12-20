from .models import Products, Category
from rest_framework import serializers
from rest_framework import exceptions
class CategorySerializer(serializers.ModelSerializer):

    class Meta : 
        model = Category
        fields = ('id', 'name')

    def validate(self, data):
        name = data['name']
        if Category.objects.filter(name=name).exists(): 
            raise exceptions.APIException('exist')
        return data

class GetProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta : 
        model = Products
        fields = (
           '__all__'
        )

class ProductSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Products
        fields = (
            'id',
            'name',
            'quantity',
            'price',
            'description',
            'availibility',
            'category',
        )
    def validate(self, data):
        name = data['name']
        if Products.objects.filter(name=name).first():
            raise exceptions.APIException('exist')
        return data

class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Products
        fields = (
            '__all__'
        )
    def validate(self, data):
        name = data['name']
        if Products.objects.filter(name=name).exclude(id=self.instance.id).first():
            raise exceptions.APIException('exist')
        return data
