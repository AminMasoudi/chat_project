import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from user.models import UsersProfile    
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        user = UsersProfile.objects.first()
        self.user = user
        self.send(json.dumps({
            'type' : 'login',
            'user': user.__str__()
        }))
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(self.user.__str__())
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message' : message,
                'sender' : self.user.__str__()
            }
        )





    def chat_message(self, event):
        message = event['message']

        self.send(json.dumps({
            'type':'chat',
            'message' : message
        }))