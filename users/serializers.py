from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserRegSerializer(serializers.ModelSerializer):

    username = serializers.RegexField(regex=r'^[A-Za-z][A-Za-z0-9._]*$',)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8, required=True,)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'role']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username already exists')
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already exists')
        return value

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token