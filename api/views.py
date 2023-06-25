from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .list import *
from .serializers import MessageSerializer, UserSerializer, RoomSerializer
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


#[ ] : permissions
@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_message(request, room_pk):
    room = Room.objects.get(pk=room_pk)
    messages = room.massage.all()
    ser_messages = MessageSerializer(messages, many=True)
    for message in ser_messages.data:
        message["origin"] = UsersProfile.objects.get(pk=message['origin']).username
    print((ser_messages.data[0]['origin']))
    return Response(ser_messages.data)

@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication]) #why??
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = UsersProfile.get_profile(request)
    ser_user = UserSerializer(user)
    return Response(ser_user.data)

@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication]) #why??
@permission_classes([IsAuthenticated])
def get_user_chats_info(request):
    rooms = UsersProfile.get_profile((request)).rooms
    ser_room = RoomSerializer(rooms, many=True)
    return Response(ser_room.data)





"""TODO
- [ ] permissions and auth
- [ ] cleaning

"""