from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer
from products.models import Products
from account.serializers import AccountSerializer
from rest_framework import exceptions
from products.serializers import GetProductSerializer, CategorySerializer

class GetOrderItemSerializer(serializers.ModelSerializer):
    product = GetProductSerializer(many=True)
    class Meta : 
        model = OrderItem
        fields = (
            'id', 
            'product',
            'quantity',
            'total',
        )

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    class Meta : 
        model = OrderItem
        fields = (
            'id', 
            'product',
            'quantity',
            'total',
        )

class POrderItemSerializer(serializers.ModelSerializer):
    class Meta : 
        model = OrderItem
        fields = (
            'id', 
            'product',
            'quantity',
            'total',
)

class OrderSerializer(serializers.ModelSerializer):
    order_item = GetOrderItemSerializer(many=True)
    user = AccountSerializer()
    class Meta : 
        model =  Order
        fields = (
            'id', 
            'address', 
            'order_item',
            'pin_code', 
            'city', 
            'paid', 
            'phone', 
            "total_price", 
            "status", 
            'user',
        )

class POrderSerializer(serializers.ModelSerializer):

    class Meta : 
        model =  Order
        fields = (
            '__all__'
        )

    def validate(self, data):
        address = data['address']
        order_item = data['order_item']
        print(1)
        print(data)
        if not address:
            print(2)
            raise exceptions.APIException('missing address')
        if not order_item:
            print(3)
            raise exceptions.APIException('missing order_item')

        return data

class PurderSerializer(serializers.ModelSerializer):

    class Meta : 
        model =  Order
        fields = (
            '__all__'
        )

class OrderInfoSerializer(serializers.ModelSerializer):
    class Meta : 
        model =  Order
        fields = (
            'id', 
            'address', 
            'pin_code', 
            'city', 
            'paid', 
            'phone', 
            "total_price", 
            "status", 
            'user',
        )  