from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import RegisterSerializer, UserSerializer, LogoutSerializer
from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from .authentication import create_access_token, create_refresh_token
from .models import Account
from rest_framework.exceptions import APIException
# Register API

class RegisterView(APIView):
    def post(self, request) :
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'results': serializer.data,
        }, status=status.HTTP_200_OK)

class LoginView(APIView):
    def post(self, request):
        print(Account.objects.all())
        user = Account.objects.filter(email=request.data['email']).first()
        print(user)
        if not user:
            raise APIException('Invalid credentials!')

        if not user.check_password(request.data['password']):
            raise APIException('Invalid password!')

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response()

        response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)
        response.data = {
            'access_token': access_token,
        }

        return response
    
class LogoutView(APIView):
    def post(self, _):
        response = Response()
        response.delete_cookie(key="refreshToken")
        response.data = {
            'message': 'success'
        }
        return response