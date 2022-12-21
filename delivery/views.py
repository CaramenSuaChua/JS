from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
#import serializer
from .serializers import DeliveryUnitSerializer,DeliverySerializer\
,PoDeliverySerializer,PuDeliverySerializer
from .pagination import get_pagination_data
#import models
from .models import DeliveryUnit, Delivery
# Create your views here.
#delivery unit
class DeliveryUnitView(APIView):
    serializer_class = DeliveryUnitSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        deli = DeliveryUnit.objects.all().values()
        return Response({
            'data': deli
        })
    
    def post(self, request):
        deli = DeliveryUnitSerializer(data= request.data)
        if deli.is_valid():
            deli.save()
            return Response({
                'data': deli.data,
                'message': 'Created successFully'
            }, status=status.HTTP_201_CREATED)
        return Response('failed', status=status.HTTP_400_BAD_REQUEST)

class DeliveryUnitDetailView(APIView):
    serializer_class = DeliveryUnitSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        deli = DeliveryUnit.objects.get(pk=pk)
        deli_obj = DeliveryUnitSerializer(deli).data
        return Response(deli_obj)

    def post(self, request, pk):
        deli = DeliveryUnit.objects.get(pk=pk)
        deli_obj = DeliveryUnitSerializer(deli, data=request.data)
        if deli_obj.is_valid():
            deli_obj.save()
            return Response(deli_obj.data)
        return Response('fail')
    
    def delete(self, request, pk):
        deli = DeliveryUnit.objects.get(pk=pk)
        deli.delete()
        return Response('delete success')

#delivery
class DeliveryView(APIView):
    serializer_class = PoDeliverySerializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        deli = Delivery.objects.all()
        deli_obj = DeliverySerializer(deli, many=True).data 
        return Response({
            'data':  get_pagination_data(request, deli_obj)
        })
    
    def post(self, request):
        deli = PoDeliverySerializer(data= request.data)
        if deli.is_valid():
            deli.save()
            return Response({
                'data': deli.data,
                'message': 'Created successFully'
            }, status=status.HTTP_201_CREATED)
        return Response('failed', status=status.HTTP_400_BAD_REQUEST)

class DeliveryDetailView(APIView):
    serializer_class = PuDeliverySerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        deli = Delivery.objects.get(pk=pk)
        deli_obj = PuDeliverySerializer(deli).data
        return Response(deli_obj)

    def put(self, request, pk):
        deli = Delivery.objects.get(pk=pk)
        deli_obj = PuDeliverySerializer(deli, data=request.data)
        if deli_obj.is_valid():
            deli_obj.save()
            return Response({
                'data': deli_obj.data,
                "message": 'Change SuccessFully'
            })
        return Response('fail')
    
    def delete(self, request, pk):
        deli = Delivery.objects.get(pk=pk)
        deli.delete()
        return Response('delete success')