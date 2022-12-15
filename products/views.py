from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductsSerializers
# Create your views here.

class ProductsView(APIView):
    model = Products
    permission_classes = [IsAuthenticated]
    def get(self, request):
        params = (
            self.request.query_params
            if len(self.request.data) == 0 
            else self.request.data
        )
        if not params.get('id'):
            pro = self.model.objects.all()
            pro_obj = ProductsSerializers(pro, many=True).data

            return Response({
                'results': pro_obj
            })
        else: 
            pro = Products.objects.get(id = params.get('id'))
            pro_obj = ProductsSerializers(pro).data

            return Response({
                'results': pro_obj
            })
        
    def post(self, request):
        params = (
            self.request.query_params
            if len(self.request.data) == 0 
            else self.request.data
        )
        pro_obj = ProductsSerializers(data = params)
        if pro_obj.is_valid():
            pro_obj.save()
            return Response({
                'results': pro_obj.data,
                'message': 'Created SuccessFully'
            }, status=status.HTTP_201_CREATED)

    def put(self, request):
        params = (
            self.request.query_params
            if len(self.request.data) == 0 
            else self.request.data
        )
        pro = Products.objects.get(id = params.get('id'))
        pro_obj = ProductsSerializers(data=params, instance=pro)
        if pro_obj.is_valid():
            # Products.objects.get(id=params.get('id'))
            pro_obj.save()
            return Response({
                'results': pro_obj.data,
                'message': 'Change SuccessFully'
            }, status=status.HTTP_200_OK)
    
    def delete(self, request):
        params = (
            self.request.query_params
            if len(self.request.data) == 0 
            else self.request.data
        )
        pro = Products.objects.get(id = params.get('id'))
        pro_obj = ProductsSerializers(data=params, instance=pro)
        if pro_obj.is_valid():
            Products.objects.get(id=params.get('id')).delete()
        return Response({
                'results': pro_obj.data,
                'message': 'Delete SuccessFully'
            }, status=status.HTTP_200_OK)