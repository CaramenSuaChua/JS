from rest_framework import serializers, exceptions

# import model 
from .models import Delivery, DeliveryUnit

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
   