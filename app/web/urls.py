from django.urls import path
from .views import others, auth

app_name = "web"

urlpatterns = [
    path("", others.IndexView.as_view(), name="index"),
    path("auth/", auth.AuthView.as_view(), name="auth")
]
