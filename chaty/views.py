from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'chaty/index.html', context)



def room(request, room_name):
    ...