from django.contrib.auth.models import User
from rest_framework import exceptions,serializers
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .models import Account
# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # password = validated_data.pop('password', None)
        # instance = self.Meta.model(**validated_data)
        # if password is not None:
        #     instance.set_password(password)
        # instance.save()
        # return instance
        user = Account.objects.create(
            name=validated_data['name'],
            password=validated_data['password'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# Login Serializer
# class LoginSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length = 100)
#     username = serializers.CharField(max_length=100, )
#     password = serializers.CharField(max_length=100, )

#     def get_token(self, obj):
#         user = User.objects.get(username=obj.username)

#         return {'refresh': user.tokens['refresh'],
#         'access': user.tokens['access']}
        
#     class Meta:
#         model = User
#         fields = ( 'username' 'password', 
#         )
    
#     def validate(self, data):
#         username = data.get('username', None)
#         password = data.get('password', None)
#         email = data.get('email', None)
        
#         if username is None:
#             raise serializers.ValidationError('username is required ')
        
#         if password is None:
#             raise serializers.ValidationError('password is require')
#         # user = authenticate(request=self.context.get('request'), username=username, password=password, email=email)
#         user = User.objects.filter(email=.data['email']).first()
#         access_token = create_access_token(user.id)     
#         user.save(access_token)  
#         if not user:
#             return Response({"error": True, "errors": "user not avaliable in our records"})
#         if not user.check_password(password):
#             return Response({"error": True, "errors": "Email and password doesnot match"})
#         data['user'] = {
#             'results':user
#         }
#         return user
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password',
            'first_name',
            'last_name',
        )

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