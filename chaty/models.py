from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)