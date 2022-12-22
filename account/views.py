from rest_framework.response import Response
from .models import User
# from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status, generics
from .serializers import CreateUserSerializer,MyTokenObtainPairSerializer,\
EmailVerificationSerializer,PasswordChangeSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import Utils
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from account import swagger
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import pyotp
from rest_framework.exceptions import PermissionDenied
# from .models import Consult
# Register API

class UsersView(APIView):
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)
    def post(self, request):
        user = request.data
        serializer = CreateUserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        print(user.password, '-------------')
        # token = RefreshToken.for_user(user).access_token

        base32secret = 'S3K3TPI5MYA2M67V'   
        token = pyotp.TOTP(base32secret)
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'http://'+current_site+relativeLink+"?OTP="+ token.now()
        email_body = 'Hi '+user.username + \
            ' Use the link below to verify your email \n' + absurl 
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}

        Utils.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)

class VerifyEmail(APIView):
    serializer_class = EmailVerificationSerializer
    permission_classes = (AllowAny,)
    token_param_config = openapi.Parameter(
        'otp', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def post(self, request):
        print(request.GET, '------')
        # username = request.data.get["username"]
        otp = request.GET.get('otp')
        print(otp)
        
        # otp = request.GET.get('otp')
        user_id = request.GET.get('id')
        try:
            # payload = jwt.decode(token, settings.SECRET_KEY)
            # payload = jwt.decode(otp, settings.SECRET_KEY)
            # print(payload, '+++++++++++++')
            user = User.objects.get(otp=otp)
            print(user, '======')
            if user.is_verified:
                user.is_verified = True
                user.save()
                return Response("Verification Successful")
            # return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        # except jwt.ExpiredSignatureError as identifier:
        #     return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        # except jwt.exceptions.DecodeError as identifier:
        #     return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        except: 
            raise PermissionDenied("OTP Verification failed")

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
            if not user.is_active:
                return Response({"error": True, "errors": "Account Disable, please contact admin"}, 
                status=status.HTTP_400_BAD_REQUEST)
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

class ChangePasswordView(APIView):
    serializer_class = PasswordChangeSerializer
    @swagger_auto_schema(
        tags=["api"],
        request_body=swagger.change_password_params,
    )
    
    def post(self, request, format=None):
        context = {'user': request.user}
        
        serializer = PasswordChangeSerializer(data=request.data, context=context)
        if serializer.is_valid():
            user = request.user
            user.set_password(request.data['new_password'])
            user.save()
            return Response(
                {"error": False, "message": "Password Changed Successfully"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"error": True, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )