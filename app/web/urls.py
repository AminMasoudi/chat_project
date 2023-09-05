from django.urls import path
from .views import others, auth

app_name = "web"

urlpatterns = [
    path("", others.IndexView.as_view(), name="index"),
    path("auth/sign_in", auth.SignInView.as_view(), name="sign_in"),
    path("auth/register", auth.RegisterView.as_view(), name="register"),
]
