from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterForm


class RegisterView(CreateView, SuccessMessageMixin):
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("home:login")
    success_message = "Your account has been created. You can now login."

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home:index")
        return super().get(request, *args, **kwargs)
