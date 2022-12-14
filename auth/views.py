from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, LogoutSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView

# Register API

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
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def retrieve(self, request: Request) -> Response:
        """Return user on GET request."""
        serializer = self.serializer_class(request.user, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request: Request, ) :
        """Return updated user."""
        serializer_data = request.data.get('user', {})

        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated ]
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = LogoutSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
