from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .models import Server, Owner


class ServerCreateView(LoginRequiredMixin, CreateView):
    model = Server
    fields = ("name", "description", "image")
    template_name = "forms/page.html"
    success_url = reverse_lazy("home:dashboard")
    extra_context = {
        "title": "Create Server",
        "description": "Create a new server.",
        "form_button_text": "Create Server"
    }

    def form_valid(self, form):
        server = form.save(commit=False)
        server.owner = Owner.objects.create(user=self.request.user)
        server.save()
        self.object = server
        return HttpResponseRedirect(self.get_success_url())


class ServerDetailView(LoginRequiredMixin, DetailView):
    model = Server
    template_name = "servers/detail.html"
    context_object_name = "server"
    pk_url_kwarg = "server_id"


class ServerEditView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Server
    fields = ("name", "description", "image")
    template_name = "forms/page.html"
    success_url = reverse_lazy("home:dashboard")
    success_message = "Server updated successfully."
    extra_context = {
        "title": "Edit Server",
        "description": "Edit your server.",
        "form_button_text": "Save Changes"
    }
