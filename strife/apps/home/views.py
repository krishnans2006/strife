from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "home/index.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "home/dashboard.html"
