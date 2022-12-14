from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import exceptions,serializers
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

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
class LoginSerializer(serializers.ModelSerializer[User]):
    email = serializers.CharField(max_length = 100)
    # username = serializers.CharField(max_length=100, read_only=True)
    # password = serializers.CharField(max_length=100, write_only= True)
    tokens = serializers.SerializerMethodField()

    def get_token(self, obj):
        user = User.objects.get(username=obj.username)

        return {'refresh': user.tokens['refresh'],
        'access': user.tokens['access']}
    
    class Meta:
        model = User
        fields = (
            'email', 'username', 'password', 'tokens', 
        )
    
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError('Email is required ')
        
        if password is None:
            raise serializers.ValidationError('password is require')
        
        user = authenticate(email = email, password = password)

        if user is None:
            raise serializers.ValidationError('email and password not found')
        
        if not user.is_active:
            raise serializers.ValidationError('user not exist')

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