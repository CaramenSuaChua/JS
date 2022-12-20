# from .models import User
from django.contrib.auth.models import User
# from .models import User
from django.contrib.auth import authenticate
from rest_framework import exceptions,serializers, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny
# Register Serializer

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            # 'first_name',
            # 'last_name',
            # 'is_active',
            # 'is_staff'
        )

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.fields["username"].required = True
        self.fields["email"].required = True
        self.fields["password"].required = False

    def validate_email(self, email):
        
        if not User.objects.filter(
                email=email).exists():
            return email
        raise serializers.ValidationError("Email already exists")

    def create(self, validate_data):
        user = User.objects.create_user(
            username = validate_data['username'],
            email= validate_data['email'],
            password= validate_data['password'],
        )
        user.save()
        return user
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        return token

# {
#     "username": "test",
#     "password": "1",
#     "email": "test1@gmail.com"
# }