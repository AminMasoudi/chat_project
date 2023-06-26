from django.urls import path, reverse

from . import views

app_name = 'chaty' 

urlpatterns = [
    path('<str:room_pk>/', views.room, name='room'),
]

