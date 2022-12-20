from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import AccSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class UserView(APIView):
    serializer_class = AccSerializer
    def post(self, request):
        acc = AccSerializer(data=request.data)
        acc.is_valid(raise_exception=True)
        acc.save()
        return Response({
            'results': acc.data,
        }, status=status.HTTP_200_OK)