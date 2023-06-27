from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from django.contrib.auth import authenticate, login

from user.models import UsersProfile
from chaty.models import Room

from .decorators import chat_message_permissions
from .serializers import MessageSerializer, UserSerializer, RoomSerializer

SIGN_IN = r"/api/sign_in/"
REGISTER = r"/api/register/"
DASHBOARD = r"/dashboard/"


@api_view(["POST"])
def register(request):

    username = request.data["username"]
    password = request.data["password"]

    if (UsersProfile.objects.filter(username=username)):
        
        return Response({
            "status": "failed",
            "msg"   : "username exist"
        })
    

    user = UsersProfile.objects.create_user(username=username, password=password)
    
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
            'user'  : user.get_username(),
            'status': 'authenticated',
            'next'  : DASHBOARD
        })
    
    
    return Response({'status':'failed'})




@api_view(["GET"])
def public_chats(request):
    rooms   = Room.objects.filter(is_private=False).all()
    ser_room= RoomSerializer(rooms, many=True)
    return Response(ser_room.data)



# @api_view(['GET'])
# @authentication_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated])
# def example_view(request, format=None):
#     user    = UsersProfile.get_profile(request)
#     rooms   = user.rooms.all()
#     ser     = UserSerializer(user)
#     return Response("1" in ser.data["rooms"])


#[ ] : permissions
@api_view(["GET"])
@chat_message_permissions
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_message(request, room_pk):
    room        = Room.objects.get(pk=room_pk)
    messages    = room.massage.order_by("time").reverse()
    ser_messages= MessageSerializer(messages, many=True)

    for message in ser_messages.data:
        message["origin"] = UsersProfile.objects.get(pk=message['origin']).username

    return Response(ser_messages.data)




@api_view(["GET"])
@authentication_classes([SessionAuthentication]) #why??
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user     = UsersProfile.get_profile(request)
    ser_user = UserSerializer(user)
    return Response(ser_user.data)




@api_view(["GET"])
@authentication_classes([SessionAuthentication]) #why??
@permission_classes([IsAuthenticated])
def get_user_private_chats(request):
    
    rooms   = UsersProfile.get_profile((request)).rooms
    ser_room= RoomSerializer(rooms, many=True)

    return Response(ser_room.data)




"""TODO
- [ ] permissions and auth
- [ ] cleaning

"""