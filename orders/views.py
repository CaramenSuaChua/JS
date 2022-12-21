from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import OrderSerializer, OrderItemSerializer,PurderSerializer,POrderItemSerializer,POrderSerializer,GetOrderItemSerializer
from rest_framework.response import Response
from .models import Order, OrderItem
from products.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from delivery.pagination import get_pagination_data
# Create your views here.
class OrderView(APIView):
    serializer_class = POrderSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        order = Order.objects.all()
        order_obj = OrderSerializer(order, many=True).data
        return Response(get_pagination_data(request, order_obj))
    
    def post(self, request):
        order = POrderSerializer(data=request.data)
        if order.is_valid():
            print(5)
            order.save()
            return Response({
                'data': order.data,
                'message': 'Create Success'
            })
        return Response('Failed')

class OrderDetailView(APIView):
    serializer_class = PurderSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        order_obj = OrderSerializer(order).data
        return Response(request,order_obj)

    def put(self, request, pk):
        order = Order.objects.get(pk=pk)
        order_obj = PurderSerializer(order, data=request.data)
        if order_obj.is_valid():
            order_obj.save()
            return Response(order_obj.data)
        return Response('fail')
    
    def delete(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response('delete success')

class OrderItemView(APIView):
    serializer_class = POrderItemSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        item = OrderItem.objects.all()
        item_obj  = GetOrderItemSerializer(item, many=True).data
        return Response(item_obj)

    def post(self, request):
        item = POrderItemSerializer(data = request.data)
        if item.is_valid():
            item.save()
            return Response(item.data)
        return Response('fail')

class OrderItemDView(APIView):
    serializer_class = POrderItemSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        item = OrderItem.objects.get(pk=pk)
        item_obj = OrderItemSerializer(item).data
        return Response(item_obj)
    
    def put(self, request, pk):
        item = OrderItem.objects.get(pk=pk)
        item_obj = POrderItemSerializer(item, data=request.data)
        if item_obj.is_valid():
            item_obj.save()
            return Response(item_obj.data)
        return Response('fail')
    
    def delete(self, request, pk):
        item = OrderItem.objects.get(pk=pk)
        item.delete()
        return Response('success')