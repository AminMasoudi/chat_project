from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data, name="index"),
    path('register/', views.new_user, name="login api"),
    path('sign_in/', views.sign_in, name='new user'),
    path("s/", views.example_view)
    
]