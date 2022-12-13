# from rest_framework.serializers import ModelSerializer
from django.db.models import F, Count
from rest_framework import serializers
from .models import Order
from products.serializers import ProductsSerializers
class OrderSerializer(serializers.Serializer):  

    def validate(self, data):
        
        return data

    def get_orders(self, data):
        pro = Order.objects.select_related('product') \
            .values('id', 'address', 
            'pin_code', 
            'city', 
            'paid', 
            'phone', 
            "total_price", 
            "status", 
            "product", 
            )
        return pro
    def get_detail_orders(self, data, pk):
        return Order.objects.get(id=pk)

    def create_product(self, data):
        try:
            Order.objects.create()
        except:
            raise serializers.ValidationError("Created unsuccessful")

class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductsSerializers()
    class Meta:
        model = Order
        fields = (
            'id', 'address', 
            'pin_code', 
            'city', 
            'paid', 
            'phone', 
            "total_price", 
            "status", 
            "product",

        )