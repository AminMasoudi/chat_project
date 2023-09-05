from django.views.generic import TemplateView
from django.urls import reverse

class SignInView(TemplateView):
    template_name = "web/sign_in.html"
    extra_context = {
        # "api" : reverse("api:sign_in")
    }

class RegisterView(TemplateView):
    template_name = "web/register.html"
