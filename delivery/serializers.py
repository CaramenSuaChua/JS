from rest_framework import serializers, exceptions
from rest_framework.response import Response
# import model 
from .models import Delivery, DeliveryUnit
from rest_framework import pagination
#import Serializer
from products.serializers import GetProductSerializer

class DeliveryUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryUnit
        fields = '__all__'

    def validate(self, data):
        name = data['name']
        phone = data['phone']
        if not name:
            raise exceptions.APIException('missing name')
        if not phone:
            raise exceptions.APIException('missing phone')
        return data
class DeliverySerializer(serializers.ModelSerializer):
    deliveryUnit = DeliveryUnitSerializer()
    products = GetProductSerializer(many=True)
    class Meta:
        model = Delivery
        fields = (
            "id",
            'products',
            "startdate",
            "deliveryUnit",
            "address"
        )

class PoDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('__all__')
    def validate(self, data):
        deliveryUnit = data['deliveryUnit']
        address = data['address']
        if not deliveryUnit:
            raise exceptions.APIException('missing deliveryUnit')
        if not address:
            raise exceptions.APIException('missing address')
        return data

class PuDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('__all__')
   
class DeliPagination(serializers.Serializer):
    page        = serializers.CharField()
    page_size   = serializers.CharField()

    def get(self, request, data):
        page = request.data['page'] 
        page_size = request.data['page_size']
        start = (int(page) * int(page_size) )
        end = start + int(page_size)

        return {
            'page': page,
            'data': data[start:end],
            'total': len(data)
        }
