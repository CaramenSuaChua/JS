from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products, Category
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .serializers import ProductSerializer, CategorySerializer,UpdateProductSerializer,GetProductSerializer
# Create your views here.
from products import swagger
from drf_yasg import openapi
class CategoryView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    @swagger_auto_schema(
        tags=["Category"],
        manual_parameters=swagger.list_category,
    )
    def get(self, request):
        cate = Category.objects.all().values().order_by('-id')
        # cate_obj = CategorySerializer(cate, many=True).data
        return Response({
            'results': cate
        })
    @swagger_auto_schema(
        tags=["Category"],
        request_body=swagger.create_category
    )
    def post(self, request):
        cate = CategorySerializer(data = request.data)
        if cate.is_valid():
            cate.save()
            return Response(cate.data)
        return Response('failed')

class CategoryDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

    @swagger_auto_schema(
        tags=["Category"],
        manual_parameters=swagger.list_detail_category,
    )
    def get(self, request, pk, *args, **kwargs, ):
        cate = Category.objects.get(pk=pk)
        cate_obj = CategorySerializer(cate).data
        return Response(cate_obj)

    @swagger_auto_schema(
        tags=["Category"],
        request_body=swagger.put_category,
    )
    def put(self, request, pk):
        cate = Category.objects.get(pk=pk)
        cate_obj = CategorySerializer(cate, data=request.data)
        if cate_obj.is_valid():
            cate_obj.save()
            return Response(cate_obj.data)
        return Response('fail')

    @swagger_auto_schema(
        tags=["Category"],
        manual_parameters=swagger.del_category,
    )
    def delete(self, request, pk):
        cate = Category.objects.get(pk=pk)
        cate.delete()
        return Response('delete success')
class ProductsView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    @swagger_auto_schema(
        tags=["Products"],
        manual_parameters=swagger.list_products,
    )
    def get(self, request):
        pro = Products.objects.all()
        pro_obj = GetProductSerializer(pro, many=True).data
        return Response({
            'results': pro_obj
        })
    @swagger_auto_schema(
        tags=["Products"],
        request_body=swagger.create_products,
    )    
    def post(self, request , *args, **kwargs):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data' : serializer.data,
                'message' : 'Create SuccessFully'
            })
        return Response({
                'data' : serializer.error_messages,
                'message' : 'Create Failed'
            })

class ProductsDetailView(APIView):
    serializer_class = ProductSerializer
    @swagger_auto_schema(
        tags=["Products"],
        manual_parameters=swagger.list_detail_products,
    )
    def get(self, request, pk):
        pro = Products.objects.get(pk=pk)
        pro_obj = GetProductSerializer(pro).data
        return Response(pro_obj)
    @swagger_auto_schema(
        tags=["Products"],
        request_body=swagger.put_products,
    )
    def put(self, request, pk):
        pro = Products.objects.get(pk=pk)
        pro_obj = UpdateProductSerializer(pro, data=request.data)
        if pro_obj.is_valid():
            pro_obj.save()
            return Response(pro_obj.data)
        return Response('fail')
    @swagger_auto_schema(
        tags=["Products"],
        manual_parameters=swagger.del_products,
    )
    def delete(self, request, pk):
        pro = Products.objects.get(pk=pk)
        pro.delete()
        return Response('success')