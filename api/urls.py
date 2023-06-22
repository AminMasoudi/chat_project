from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data, name="index"),
    path('auth/', views.auth, name="login api"),
    path('sign_in/', views.new_user, name='new user'),
    
]