from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.views import auth

router = DefaultRouter()
router.register("auth",
                auth.RegisterViewSet,
                "auth")


app_name = "api"

urlpatterns = [
    path("", include(router.urls))
]

