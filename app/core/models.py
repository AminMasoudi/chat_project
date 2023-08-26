from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra):
        user = self.model(email=self.normalize_email(email), **extra) 
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password,**extra):
        user = self.create_user(email=email, password=password, **extra)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    
class User(AbstractUser, PermissionsMixin):
    ...
    chats = models.ManyToManyField("core.Chat", verbose_name=_("Users Chat"), related_name="members")


class Chat(models.Model):

    name = models.CharField(_("Chat Name"), max_length=50)
    

    class Meta:
        verbose_name = _("chat")
        verbose_name_plural = _("chats")

    def __str__(self):
        return self.name
