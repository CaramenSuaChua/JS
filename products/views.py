from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products, Category
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from .serializers import ProductSerializer, CategorySerializer,UpdateProductSerializer,GetProductSerializer
# Create your views here.

class CategoryView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    def get(self, request):
        cate = Category.objects.all().values()
        # cate_obj = CategorySerializer(cate, many=True).data
        return Response({
            'results': cate
        })
    
    def post(self, request):
        cate = CategorySerializer(data = request.data)
        if cate.is_valid():
            cate.save()
            return Response(cate.data)
        return Response('failed')

class CategoryDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    def get(self, request, pk, *args, **kwargs, ):
        cate = Category.objects.get(pk=pk)
        cate_obj = CategorySerializer(cate).data
        return Response(cate_obj)
    
    def post(self, request, pk):
        cate = Category.objects.get(pk=pk)
        cate_obj = CategorySerializer(cate, data=request.data)
        if cate_obj.is_valid():
            cate_obj.save()
            return Response(cate_obj.data)
        return Response('fail')
    
    def delete(self, request, pk):
        cate = Category.objects.get(pk=pk)
        cate.delete()
        return Response('delete success')
class ProductsView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    def get(self, request):
        pro = Products.objects.all()
        pro_obj = GetProductSerializer(pro, many=True).data
        return Response({
            'results': pro_obj
        })
        
    def post(self, request , *args, **kwargs):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data' : serializer.data,
                'message' : 'Create SuccessFully'
            })
        return Response({
                'data' : serializer.data,
                'message' : 'Create Failed'
            })

class ProductsDetailView(APIView):
    serializer_class = ProductSerializer
    def get(self, request, pk):
        pro = Products.objects.get(pk=pk)
        pro_obj = GetProductSerializer(pro).data
        return Response(pro_obj)
    
    def put(self, request, pk):
        pro = Products.objects.get(pk=pk)
        pro_obj = UpdateProductSerializer(pro, data=request.data)
        if pro_obj.is_valid():
            pro_obj.save()
            return Response(pro_obj.data)
        return Response('fail')
    
    def delete(self, request, pk):
        pro = Products.objects.get(pk=pk)
        pro.delete()
        return Response('success')