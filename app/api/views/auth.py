from django.contrib.auth import login, authenticate

from rest_framework.generics import GenericAPIView
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status
from rest_framework import exceptions
from rest_framework.response import Response

from api import serializers


class BaseAuth:

    serializer_class = serializers.UserSerializer

    def perform_create(self, serializer):
        serializer.save()


class AuthViewSet(
    BaseAuth,
    viewsets.ViewSet,
    GenericAPIView,
                  ):
    

    @action(methods=["POST"], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )
        
    
