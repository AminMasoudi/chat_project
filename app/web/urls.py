from django.urls import path
from .views import others

app_name = "web"

urlpatterns = [
    path("", others.IndexView.as_view(), name="index")
]
