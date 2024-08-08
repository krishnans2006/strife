from django.contrib.auth import logout
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView

from .forms import RegisterForm, LoginForm


class LoginView(DjangoLoginView):
    template_name = "users/login.html"
    form_class = LoginForm
    redirect_authenticated_user = True


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("users:login")
    success_message = "Your account has been created. You can now login."

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home:index")
        return super().get(request, *args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect("users:login")
