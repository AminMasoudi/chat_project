from django.urls import path

from . import views

# appname = 'chaty' 

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]