from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .decorators import check_permission


# Create your views here.

@login_required(login_url="/sign_in")
@check_permission
def room(request, room_pk):
    return render(request, "chaty/chatroom.html",{
        "room_pk" : room_pk
    })