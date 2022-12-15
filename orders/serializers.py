from rest_framework.serializers import ModelSerializer
from .models import Order
from products.serializers import ProductsSerializers
class OrderSerializer(ModelSerializer):
    products = ProductsSerializers()
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
            "product", 
        )