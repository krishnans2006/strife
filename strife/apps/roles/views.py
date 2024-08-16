from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView

from ..permissions.forms import PermissionsForm
from ..servers.models import Server
from .forms import RoleForm
from .models import Role


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
        "form_button_text": "Create Role",
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


def role_edit_view(request, server_id, role_id):
    role = Role.objects.get(id=role_id)

    if request.method == "POST":
        role_form = RoleForm(request.POST, instance=role, prefix="role")
        permissions_form = PermissionsForm(
            request.POST, instance=role.permissions, prefix="permissions"
        )
        if role_form.is_valid() and permissions_form.is_valid():
            role_form.save()
            permissions_form.save()
            return redirect("servers:roles:edit", server_id=server_id, role_id=role_id)
    else:
        role_form = RoleForm(instance=role, prefix="role")
        permissions_form = PermissionsForm(instance=role.permissions, prefix="permissions")

    return render(
        request,
        "roles/edit.html",
        {
            "server": role.server,
            "role": role,
            "is_default_role": False,
            "role_form": role_form,
            "permissions_form": permissions_form,
        },
    )


def default_role_edit_view(request, server_id):
    server = Server.objects.get(id=server_id)
    permissions = server.permissions

    if request.method == "POST":
        form = PermissionsForm(request.POST, instance=permissions, prefix="permissions")
        if form.is_valid():
            form.save()
            return redirect("servers:roles:edit_default", server_id=server_id)
    else:
        form = PermissionsForm(instance=permissions, prefix="permissions")

    return render(
        request,
        "roles/edit_default.html",
        {
            "server": server,
            "form": form,
            "is_default_role": True,
        },
    )


class RoleDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Role
    template_name = "forms/page.html"
    pk_url_kwarg = "role_id"
    success_message = "Role deleted successfully."
    extra_context = {
        "title": "Delete Role",
        "description": "Are you sure you want to delete this role?",
        "form_button_text": "Delete Role",
    }

    def get_success_url(self):
        return reverse("servers:roles:index", kwargs={"server_id": self.kwargs.get("server_id")})
