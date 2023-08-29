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


class GroupChat(BaseModel):

    name = models.CharField(_("Chat Name"), max_length=50)
    users = models.ManyToManyField("core.User",
                                   verbose_name=_("Users"),
                                   related_name="group_chats")


    class Meta:
        verbose_name = _("Group chat")
        verbose_name_plural = _("Group chats")


    
class PersonalChat(BaseModel):
    users = models.ManyToManyField("core.User",
                                   verbose_name=_("Users"),
                                   related_name="pvs")
    
    class Meta:
        verbose_name = _("Personal chat")
        verbose_name_plural = _("Personal chats")