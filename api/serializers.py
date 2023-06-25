from rest_framework import serializers
from chaty.models import Massage, Room
from user.models import UsersProfile
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Massage
        fields = ['id', 'origin', "destination", "content"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersProfile
        fields = ['username', 'rooms', 'date_joined', ]
        

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['pk', 'name', 'is_private']
