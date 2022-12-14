from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, LogoutSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from .authentication import create_access_token
# Register API
from django.contrib.auth import authenticate
class RegisterView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request) :
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'results': serializer.data,
        }, status=status.HTTP_200_OK)


class LoginView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        # access_token = create_access_token(user.id)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'results': serializer.data,
            
        }, status=status.HTTP_200_OK)

class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated ]

    def post(self, request):
        serializer = LogoutSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
