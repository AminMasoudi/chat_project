from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .list import *
from .serializers import MessageSerializer
from user.models import UsersProfile
from chaty.models import Room, Massage
from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer

@api_view(['GET'])
def get_data(request):
    person = {'name': 'amin'}
    return Response(person)


@api_view(["POST"])
def new_user(request):
    #TODO auth 
    username_ = request.data["username"]
    password_ = request.data["password"]
    if (UsersProfile.objects.filter(username=username_)):
        return Response({
            "status" : "failed",
            "msg" : "username exist"
        })
    user = UsersProfile.objects.create_user(username=username_, password=password_)
    login(request, user)
    return Response({
        "status" : "success",
        "msg": "",
        "next": DASHBOARD
    })

@api_view(["POST"])
def sign_in(request):
    username = request.data["username"]
    password = request.data["password"]
    user = authenticate(request, username=username, password=password,)
    if user:
        login(request, user)
        return Response({
            'user' : user.get_username(),
            'status' : 'authenticated',
            'next': DASHBOARD
        })
    return Response({'status':'failed'})


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)

#TODO : permissions
@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_message(request, room_pk):
    room = Room.objects.get(pk=room_pk)
    messages = room.massage.all()
    ser_messages = MessageSerializer(messages, many=True)
    return Response(ser_messages.data)

