from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name="index"),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('register/', views.register, name="register"),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
]