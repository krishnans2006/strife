from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, CreateView


class IndexView(TemplateView):
    template_name = "home/index.html"
