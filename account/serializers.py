from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import exceptions
class AccSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    
    def create(self, validated_data):
        username = validated_data['username']
        password=validated_data['password']
        email=validated_data['email']
        if email & username:
            raise exceptions.APIException('Email and Username is exist')
        user = User.objects.create(
            username=username,
            password=password,
            email=email,
        )
        user.set_password(password)
        user.save()
        return user

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',]