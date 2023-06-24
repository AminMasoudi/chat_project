from django.shortcuts import render
from chaty.models import Room
from django.http import HttpResponseForbidden
from user.models import UsersProfile, User

def check_permission(view):
    def wrapper(request,room_pk):
        r = Room.objects.filter(pk=room_pk).first()
        if (not request.user.is_authenticated) or not r:
            return HttpResponseForbidden({"msg1" :"permission denied"})
        profile = UsersProfile.objects.get(username=request.user.username)
        if profile.rooms.filter(pk=r.id) :
            return view(request, room_pk)
        return HttpResponseForbidden({"msg" :"permission denied"})

    return wrapper


# Create your views here.

def index(request):
    context = {}
    return render(request, 'chaty/index.html', context)


@check_permission
def room(request, room_pk):
    return render(request, "chaty/chatroom.html",{
        "room_pk" : room_pk
    })