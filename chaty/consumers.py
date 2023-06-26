import json
from channels.generic.websocket import WebsocketConsumer
from channels.http import HttpResponse
from asgiref.sync import async_to_sync
from chaty.models import Massage, Room
from user.models import UsersProfile


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        
        self.room_group_name = self.scope['path'].split("/")[-1]
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.room = Room.objects.get(pk=self.room_group_name)
        self.accept()
        
        self.user = UsersProfile.objects.get(pk=self.scope['user'].pk)
        self.send(json.dumps({
            'type' : 'login',
            'user': self.user.__str__()
        }))
        
            


    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        Massage.objects.create(origin=self.user,
                               destination=self.room,
                               content=message)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message' : message,
                'sender' : self.user.__str__(),
            }
        )



    def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        self.send(json.dumps({
            'type':'chat',
            'message' : message,
            'sender': sender
        }))


