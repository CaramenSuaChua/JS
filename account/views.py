from rest_framework.response import Response
from .models import User
# from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, generics
from .serializers import CreateUserSerializer,MyTokenObtainPairSerializer,\
EmailVerificationSerializer,PasswordChangeSerializer,RequestPasswordResetEmailSerializer\
,SetNewPasswordSerializer
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
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, DjangoUnicodeDecodeError,smart_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Utils
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
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
        uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
        print(user.password, '-------------')
        base32secret = 'S3K3TPI5MYA2M67V'   
        otp = pyotp.TOTP(base32secret)
        user.otp = otp.now()
        user.save()
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'http://'+current_site + relativeLink 
        email_body = 'Hi '+user.username + \
            ' Use the link below to verify your email \n' + absurl 
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}
        Utils.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)

class VerifyEmail(APIView):
    serializer_class = EmailVerificationSerializer
    permission_classes = (AllowAny,)
        
    @swagger_auto_schema(request_body= openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties= {
            'otp': openapi.Schema(type=openapi.TYPE_STRING),
            'uidb64': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING)
        }
    ))
    def post(self, request, otp, uidb64):
        try:
            serializer = EmailVerificationSerializer(data = request.data)
            # print(serializer.data['email'], '++++++++++++++++=')
            # if serializer.is_valid(raise_exception=True):
            #     print(otp)
            #     email = serializer.data['email']
            #     user = User.objects.filter(email = email)
            #     if not user.exists():
            #              return Response({
            #         'errors': 'uibdb64 is not valid, ',
            #         }, status=status.HTTP_400_BAD_REQUEST)
            #     if  otp != serializer.data['otp']:
            #           return Response({
            #         'errors': 'otp is not valid, ',
            #         }, status=status.HTTP_400_BAD_REQUEST)

            #     user[0].is_verified = True
            #     user[0].save()
            #     return Response({
            #         'errors': 'success, ',
            #         }, status=status.HTTP_200_OK)
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.filter(id=id)
            print(user, '-------------+++++++-')
            if len(otp) != 6:
                return Response({
                    'errors': 'otp is not valid, ',
                }, status=status.HTTP_400_BAD_REQUEST)
            if PasswordResetTokenGenerator().check_token(user, otp):
                return Response({
                    'errors': 'otp is not valid, please request a new one',
                }, status=status.HTTP_400_BAD_REQUEST)
            return Response({
                'errors': False,
                'message': 'User Activate SuccessFully'
            }, status=status.HTTP_200_OK)
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

class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = RequestPasswordResetEmailSerializer

    def post(self, request):
        serializer = RequestPasswordResetEmailSerializer(data = request.data)
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            base32secret = 'S3K3TPI5MYA2M67V'   
            otp = pyotp.TOTP(base32secret)
            user.otp = otp.now()
            user.save()
            current_site = get_current_site(request = request).domain
            relativeLink = reverse('password-reset-confirm', kwargs={'uidb64': uidb64,'otp': otp.now()})
            absurl = 'http://'+current_site+relativeLink
            email_body = 'Hello, \
                Use the link below to reset your password \n' + absurl 
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your password'}

            Utils.send_email(data)
        return Response({'success': 'We have sent you a link to reset your password'},
         status=status.HTTP_200_OK)
class PasswordCheckTokenAPI(generics.GenericAPIView):

    def get(self, request, otp, uidb64):
        try:
            print(otp, '-------')
            print(uidb64, '-------')
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id = id)
            print(user, '==========')
            if len(otp) != 6:
                return Response({
                    'errors': 'otp is not valid, ',
                }, status=status.HTTP_400_BAD_REQUEST)
            if PasswordResetTokenGenerator().check_token(user, otp):
                return Response({'error': 'otp is not valid, please request a new one'},
                  status=status.HTTP_400_BAD_REQUEST)

            return Response({
                'success': True, 
                'message':'Credentials Valid',
                'uidb64': uidb64,
                'otp': otp,
                },status=status.HTTP_200_OK)
        except DjangoUnicodeDecodeError :
            # print(1)
            # if not PasswordResetTokenGenerator().check_token(user):
            return Response({'error': 'OTP is not valid, please request a new one'},
                  status=status.HTTP_400_BAD_REQUEST)

class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = SetNewPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({
                'error': False,
                'message': 'Password reset success'
            },status=status.HTTP_200_OK)
        return Response({
                'error': True,
                'message': 'Password reset failed'
            },status=status.HTTP_200_OK)