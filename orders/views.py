from django.shortcuts import render
from .models import Order
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import OrderSerializer
# Create your views here.

class OrdersView(APIView):
    model = Order

    def get(self, request, *args, **kwargs ):
        params = (
            self.request.query_params
            if len(self.request.data) == 0
            else self.request.data
        )
        if not params.get('id'):
            order = Order.objects.all()
            order_obj = OrderSerializer(order, many=True).data
            return Response({
                'results': order_obj
            })
        else :
            order = Order.objects.get(id = params.get('id'))
            order_obj = OrderSerializer(order).data
            return Response({
                'results': order_obj
            })
        
    def post(self, request):
        params = (
            self.request.query_params
            if len(self.request.data) == 0 
            else self.request.data
        )
        order_obj = OrderSerializer(data=params)
        if order_obj.is_valid():
            order_obj.save()
            return Response({
            'results': order_obj.data,
            'message': 'Created Successfully'
        }, status=status.HTTP_201_CREATED)
    
    def put(self, request):
        params = (
            self.request.query_params
            if len(self.request.data) == 0 
            else self.request.data
        )
        order = Order.objects.get(id= params.get('id'))
        order_obj = OrderSerializer(data=params, instance=order)
        if order_obj.is_valid():
            order_obj.save()
            return Response({
            'results': order_obj.data,
            'message': 'Change Successfully'
        }, status=status.HTTP_200_OK)

    def delete(self, request):
        params = (
            self.request.query_params
            if len(self.request.data) == 0 
            else self.request.data
        )
        if not params.get('id'):
            return Response({ "error": True ,"message": "Chưa nhập mã don hang"})
        order = Order.objects.get(id= params.get('id'))
        order_obj = OrderSerializer(data=params, instance=order)
        if order_obj.is_valid():
            Order.objects.get(id=params.get('id')).delete()
            return Response({
            'message': 'Delete Successfully'
        }, status=status.HTTP_200_OK)