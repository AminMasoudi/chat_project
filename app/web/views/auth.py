from django.views.generic import TemplateView
from django.urls import reverse
class AuthView(TemplateView):
    template_name = "web/auth.html"
    extra_context = {
        # "login": reverse("api:login"),    #TODO add login api
        # "register" : reverse("api:register") #TODO add register api
    }