from django.db import models
from django.contrib.auth.models import User
from chaty.models import Room
# Create your models here.



class UsersProfile(User):
    name = models.CharField(max_length=64, blank=True)
    #TODO add through to rooms
    rooms = models.ManyToManyField(Room, blank=True, related_name="member")
    
    def get_profile(request):
        if request.user.is_authenticated:
            return UsersProfile.objects.get(pk=request.user.pk)
