from django.shortcuts import render
from api.list import *
from django.http import HttpResponseRedirect
from .helpers import log_user_in, register_user
from django.urls import reverse
from django.contrib.auth import logout
# Create your views here.




def index(request):
    return render(request, 'user/index.html')


def dashboard(request):
    return render(request, 'user/dashboard.html', {
        'groups_api': GROUP_API,
        'chat_api'  : CHAT_API,
        'user_info' : USER_INFO 
    })




def sign_in(request):
    if request.method == "POST":
        return log_user_in(request)
    
    return render(request, "user/sign_in.html", {
        "sign_in_api" : SIGN_IN,

    })


    
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("user:sign_in"))


def register(request):
    if request.method == "POST":
        return register_user(request)

    if request.user.is_authenticated:
        logout(request)
    return render(request, "user/register.html", {
        "register_api": REGISTER
    })

