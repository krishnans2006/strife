from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView as DjangoLoginView

from .forms import RegisterForm, LoginForm, UpdateProfileForm


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


class EditView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "users/edit.html"
    form_class = UpdateProfileForm
    success_url = reverse_lazy("home:dashboard")
    success_message = "Your profile has been updated."

    def get_object(self, queryset=None):
        return self.request.user


def logout_view(request):
    logout(request)
    return redirect("users:login")
