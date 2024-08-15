from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .models import Role
from ..servers.models import Server


class RoleCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Role
    fields = ("name", "description", "color")
    template_name = "forms/page.html"
    success_url = reverse_lazy("home:dashboard")
    success_message = "Role created successfully."
    extra_context = {
        "title": "Create Role",
        "description": "Create a new role.",
        "form_button_text": "Create Role"
    }


class RoleEditView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Role
    fields = ("name", "description", "color")
    template_name = "forms/page.html"
    pk_url_kwarg = "role_id"
    success_url = reverse_lazy("home:dashboard")
    success_message = "Role updated successfully."
    extra_context = {
        "title": "Edit Role",
        "description": "Edit your role.",
        "form_button_text": "Save Changes"
    }
