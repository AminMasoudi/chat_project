from django.db import models
from django.contrib.auth.models import User
from chaty.models import Group
# Create your models here.



class UsersProfile(User):
    #TODO: 
    #groups = models.ManyToManyField(Group,blank=True, related_name='members')
    pass

class Foo(models.Model):
    ...