from django.contrib.auth.hashers import make_password

from rest_framework import serializers, exceptions

from core.models import User
class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        
    def validate_username(self, username):
        if User.objects.filter(username=username).first():
            raise exceptions.AuthenticationFailed("username exist")
        return username
    