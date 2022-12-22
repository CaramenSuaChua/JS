# from django.contrib.auth.models import User
from .models import User
# from account.models import UserModel
from rest_framework import serializers,exceptions
from rest_framework import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import check_password
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',]


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
        # self.fields["first_name"].required = False
        # self.fields["last_name"].required = False
        # self.fields["is_active"].required = False
        # self.fields["is_staff"].required = False

    def validate_email(self, email):
        
        if not User.objects.filter(
                email=email).exists():
            return email
        raise serializers.ValidationError("A user with that email already exists")

    def create(self, validate_data):
        user = User.objects.create(
            username = validate_data['username'],
            email= validate_data['email'],
            password= validate_data['password'],
            # first_name = validate_data['first_name'],
            # last_name= validate_data['last_name'],
            # is_active= validate_data['is_active'],
            # is_staff= validate_data['is_staff'],
        )
        user.set_password(validate_data['password'])
        user.save()
        return user

class EmailVerificationSerializer(serializers.ModelSerializer):
    otp = serializers.CharField(max_length=555)
    username = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['otp', 'username', ]

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        return token

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=100)
    new_password = serializers.CharField(max_length=100)
    retype_password = serializers.CharField(max_length=100)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate_old_password(self, pwd):
        if not check_password(pwd, self.context.get('user').password):
            raise serializers.ValidationError(
                "old password entered is incorrect.")
        return pwd

    def validate(self, data):
        
        if len(data['new_password']) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long!")
        if data['new_password'] == data['old_password']:
            raise serializers.ValidationError(
                "New_password and old password should not be the same")
        if data['new_password'] != data['retype_password']:
            raise serializers.ValidationError(
                "New_password and Retype_password did not match.")
        return data
