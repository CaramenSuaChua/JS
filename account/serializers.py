# from django.contrib.auth.models import User
from .models import User
from rest_framework import serializers, exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import check_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, DjangoUnicodeDecodeError,smart_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
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

class EmailVerificationSerializer(serializers.Serializer):
    otp = serializers.CharField()
    uidb64 = serializers.CharField( )
    email = serializers.EmailField( )
     

    class Meta:
        fields = ['otp', 'email' ]
    

   

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

class RequestPasswordResetEmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(min_length=5)

    class Meta:
        model = User
        fields = ['email', ]

class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    otp = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'otp', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs['password']
            otp = attrs['otp']
            uidb64 = attrs['uidb64']
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            print(user)
            if PasswordResetTokenGenerator().check_token(user, otp):
                raise exceptions.AuthenticationFailed('a The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            print(user, '+++++++++')
            return (user)
        except Exception as e:
            raise exceptions.AuthenticationFailed('1The reset link is invalid', 401)
        