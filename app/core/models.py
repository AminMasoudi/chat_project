from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.
    
class User(AbstractUser, PermissionsMixin):
    ...


class Chat(models.Model):

    name = models.CharField(_("Chat Name"), max_length=50)
    

    class Meta:
        verbose_name = _("chat")
        verbose_name_plural = _("chats")

    def __str__(self):
        return self.name
