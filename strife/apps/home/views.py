from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView as DjangoLoginView


class IndexView(TemplateView):
    template_name = "home/index.html"


class LoginView(DjangoLoginView):
    template_name = "home/login.html"
    redirect_authenticated_user = True
