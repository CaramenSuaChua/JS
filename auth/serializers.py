from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import exceptions,serializers
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(max_length = 50)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'is_staff'
        )
    def create(self, validate_data):
        user = User.objects.create_user(
            username = validate_data['username'],
            email= validate_data['email'],
            password= validate_data['password'],
            is_staff= validate_data['is_staff']
        )
        user.save()
        return user

# Login Serializer
class LoginSerializer(TokenObtainPairSerializer):
    email = serializers.CharField(max_length = 100)
    username = serializers.CharField(max_length=100, )
    password = serializers.CharField(max_length=100, )
    token = serializers.SerializerMethodField()

    def get_token(cls, user):
        token = super(LoginSerializer, cls).get_token(user)

        # Add custom claims
        return token
    
    class Meta:
        model = User
        fields = (
            'email', 'username', 'password', 'token', 
        )
    
    def validate(self, data):
        email = data.get('email', )
        password = data.get('password', )
        if email is None:
            raise serializers.ValidationError('Email is required ')
        
        if password is None:
            raise serializers.ValidationError('password is require')
        
        user = authenticate(email = email, password = password)
        if not user:
            return Response({"error": True, "errors": "user not avaliable in our records"})
        if not user.check_password(password):
            return Response({"error": True, "errors": "Email and password doesnot match"})

        return data
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password',
            'tokens'
        )
        read_only_fields = 'tokens'

#Logout Serializer
class LogoutSerializer(serializers.ModelSerializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError as er: 
            raise exceptions.AuthenticationFailed(er)