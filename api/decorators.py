from user.models import UsersProfile
from chaty.models import Room
from django.http import HttpResponseForbidden


def chat_message_permissions(func):
    def wrapper(request, room_pk):
        room = Room.objects.filter(pk=room_pk).first()
        user = UsersProfile.get_profile(request)
        if room and room.have_permission(user): 
            return func(request, room_pk)
        return HttpResponseForbidden("permission denied")
    return wrapper

        