from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    # auth
    path('register/', views.register, name="login api"),
    path('sign_in/', views.sign_in, name='new user'),
    # chat info
    path('get_messages/<str:room_pk>', views.get_message, name='get_message'), # need to check permissions
    path("get_chats_info", views.get_user_private_chats, name="user_chats"),
    path("public_chats", views.public_chats, name="public_chats"),
    path("get_user_info", views.get_user_info),

    path("test", views.example_view)
]