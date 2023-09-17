from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from core.models import User
class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        
    def validate_username(self, username):
        return username
    
    def is_valid(self, *, raise_exception=False):
        return super().is_valid(raise_exception=raise_exception)
        