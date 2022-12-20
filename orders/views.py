from django.shortcuts import render
from .models import Order
from django.http import HttpResponse
# from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView, Response
from .serializers import OrderSerializer, OrderDetailSerializer
# Create your views here.
from rest_framework.permissions import IsAuthenticated

class OrdersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        params = (
            self.request.query_params
            if len(self.request.data) == 0
            else self.request.data
        )
        
        serializer = OrderSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        list_order = serializer.get_orders(serializer.data)
        return Response(data=list_order, status=200)
        
    def post(self, request):
        data = (
            self.request.query_params
            if len(self.request.data) == 0 
            else self.request.data
        )
        serializer = OrderSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        serializer.create_product(serializer.data)
        return Response("Created success", status=200)

        # if not serializer.is_valid():
        #     serializer.save()
        #     return Response({
        #     'results': serializer.data,
        #     'message': 'Created Successfully'
        # }, status=status.HTTP_201_CREATED)
    
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

class OrderDetailView(APIView):

    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        serializer = OrderDetailSerializer(order)
        print(serializer.data)
        # if not serializer.is_valid():
        #     return Response(serializer.errors, status=400)
        # order = serializer.get_detail_orders(serializer.data, pk)
        return Response(serializer.data, status=200)  