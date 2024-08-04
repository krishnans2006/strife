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


class RegisterView(CreateView, SuccessMessageMixin):
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("users:login")
    success_message = "Your account has been created. You can now login."

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home:index")
        return super().get(request, *args, **kwargs)


class LogoutView(DjangoLogoutView, SuccessMessageMixin):
    next_page = reverse_lazy("users:login")
    success_message = "You have been logged out."
