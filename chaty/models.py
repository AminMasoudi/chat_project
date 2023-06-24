from django.db import models
# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=64, unique=True, auto_created=True)
    is_private = models.BooleanField(default=True)

from user.models import UsersProfile

class Massage(models.Model):
    origin = models.ForeignKey(UsersProfile, on_delete=models.DO_NOTHING, related_name="+")
    destination = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="massage")
    content = models.TextField(max_length=1024)
    time = models.TimeField(auto_now=True)

    class Meta:
           ordering = ['time'] 