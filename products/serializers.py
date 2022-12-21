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

    creator = serializers.ReadOnlyField(source='creator.username')
    creator_id = serializers.ReadOnlyField(source='creator.id')
    image_url = serializers.ImageField(required=False)

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
            'creator',
            'creator_id',
            'image_url'
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
