from django.http import HttpResponseForbidden, HttpResponseNotFound
from .models import Room, UsersProfile
# from user.models import UsersProfile





def check_permission(view):
    def wrapper(request,room_pk): 
        room = Room.objects.filter(pk=room_pk).first()
        user = UsersProfile.get_profile(request)
        if not room:
            return HttpResponseNotFound("Not Find")  
        elif room.have_permission(user):
            return view(request, room_pk)
        return HttpResponseForbidden({"msg" :"permission denied"})

    return wrapper
