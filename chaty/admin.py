from django.contrib import admin
from.models import *
# Register your models here.

class MassageAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "content", "time")

class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_private", "member")

admin.site.register(Massage, MassageAdmin)
admin.site.register(Room, RoomAdmin)