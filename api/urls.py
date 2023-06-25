from django.urls import path
from . import views

urlpatterns = [
    # path('', views.get_data, name="index"),
    path("s/", views.example_view),
    path('register/', views.new_user, name="login api"),
    path('sign_in/', views.sign_in, name='new user'),
    path('get_messages/<str:room_pk>', views.get_message, name='get_message'),
    path("get_chats_info", views.get_user_chats_info),
    path("get_user_info", views.get_user_info),
]