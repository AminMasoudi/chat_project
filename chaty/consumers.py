import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from user.models import UsersProfile    
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = self.scope['path'].split("/")[-1]
        self.user = self.scope['user']
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
        print(self.scope['user'].username)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message' : message,
                'sender' : self.scope['user'].username,
                'in': self.room_group_name
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



"""
TODO : 
- [ ] cleanning this mess
- [ ] add new messages to db

"""