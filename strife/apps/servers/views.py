from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .models import Server, Owner


class ServerCreateView(CreateView, LoginRequiredMixin):
    model = Server
    fields = ("name", "description", "image")
    template_name = "forms/create.html"
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


class ServerDetailView(DetailView, LoginRequiredMixin):
    model = Server
    template_name = "servers/detail.html"
    context_object_name = "server"
