from rest_framework import serializers
from .models import Products

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = (
            '__all__'
        )

class ProSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Products
        fields = (
            '__all__'
        )
    def validate(self, data):
        
        return data

    def create_pro(self, request, data):
        try:
            return Products.objects.create(
                name=data['name'],
                quantity=data['quantity'],
                price=data['price'],
                desciption=data['desciption'],
                )
            
        except:
            raise serializers.ValidationError('Create faild')