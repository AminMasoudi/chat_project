from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "web/index.html"
    extra_context = None
    
