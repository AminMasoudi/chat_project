from rest_framework import serializers
from chaty.models import Massage, Room

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Massage
        fields = '__all__'
        