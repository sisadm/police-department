from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    username = serializers.RegexField(regex=r'^[A-Za-z][A-Za-z0-9._]*$',)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'role']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username already exists')
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already exists')
        return value


