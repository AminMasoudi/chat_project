from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.
    
class User(AbstractUser, PermissionsMixin):
    ...


class BaseModel(models.Model):
    create_date     = models.DateTimeField(_("Creation Date"), auto_now_add=True)
    updated_date    = models.DateTimeField(_("Update Date"), auto_now=True)

    class Meta:
        abstract = True

