from audioop import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView

from .models import Role
from ..servers.models import Server


class RoleIndexView(LoginRequiredMixin, ListView):
    model = Role
    template_name = "roles/index.html"
    context_object_name = "roles"
    paginate_by = 10

    def get_queryset(self):
        server_id = self.kwargs.get("server_id")
        server = Server.objects.get(id=server_id)

        return Role.objects.filter(server=server)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["server"] = Server.objects.get(id=self.kwargs.get("server_id"))
        return context


class RoleCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Role
    fields = ("name", "description", "color")
    template_name = "forms/page.html"
    success_message = "Role created successfully."
    extra_context = {
        "title": "Create Role",
        "description": "Create a new role.",
        "form_button_text": "Create Role"
    }

    def get_success_url(self):
        return reverse("servers:roles:index", kwargs={"server_id": self.kwargs.get("server_id")})

    def form_valid(self, form):
        role = form.save(commit=False)

        server_id = self.kwargs.get("server_id")
        server = Server.objects.get(id=server_id)

        role.server = server
        role.save()

        self.object = role

        return HttpResponseRedirect(self.get_success_url())


class RoleEditView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Role
    fields = ("name", "description", "color")
    template_name = "roles/edit.html"
    pk_url_kwarg = "role_id"
    success_message = "Role updated successfully."
    extra_context = {
        "title": "Edit Role",
        "description": "Edit your role.",
        "form_button_text": "Save Changes"
    }

    def get_success_url(self):
        return reverse("servers:roles:edit", kwargs={"server_id": self.kwargs.get("server_id"), "role_id": self.kwargs.get("role_id")})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["server"] = Server.objects.get(id=self.kwargs.get("server_id"))
        return context


class RoleDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Role
    template_name = "forms/page.html"
    pk_url_kwarg = "role_id"
    success_message = "Role deleted successfully."
    extra_context = {
        "title": "Delete Role",
        "description": "Are you sure you want to delete this role?",
        "form_button_text": "Delete Role"
    }

    def get_success_url(self):
        return reverse("servers:roles:index", kwargs={"server_id": self.kwargs.get("server_id")})
