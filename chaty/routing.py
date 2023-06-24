from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/socket-server/', consumers.ChatConsumer.as_asgi()),
    # re_path(r'ws/socket-server/<int:room_pk>', consumers.RoomConsumer.as_asgi())
]