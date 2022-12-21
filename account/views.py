from rest_framework.response import Response
# from .models import User
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from .serializers import CreateUserSerializer,MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Register API

class UsersView(APIView):
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'results': serializer.data,
        }, status=status.HTTP_200_OK)


class ObtainTokenPairWithColorView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
   
    def post(self, request):
        params = request.query_params if len(
            request.data) == 0 else request.data
        username = params.get("username", None)
        password = params.get("password", None)
        print(username, password, '++++++++++++')
        if not username:
            return Response({'error': True, 'username': "This field is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({'error': True, 'pass': "This field is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.filter(username=username).first()
            print(user, '-------------------')
            if not user:
                return Response({"error": True, "errors": "username not avaliable in our records"}, status=status.HTTP_400_BAD_REQUEST)
            if not user.check_password(password): 
                return Response({"error": True, "errors": "Password doesnot match"}, status=status.HTTP_400_BAD_REQUEST)

            serializer = self.get_serializer(data=request.data)
            print(serializer, '==============')
            try:
                serializer.is_valid(raise_exception=True)
            except :
                return Response({"error": True, "errors": "user login not avaliable in our records"}, status=status.HTTP_400_BAD_REQUEST)
            return Response( serializer.validated_data,
             status=status.HTTP_200_OK)
        except: 
            return Response({"error": True, "errors": "user login failed"}, status=status.HTTP_400_BAD_REQUEST)

class DecoratedTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)