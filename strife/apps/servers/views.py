from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Server


class ServerCreateView(CreateView):
    model = Server
    fields = ("name", "description", "image")
    template_name = "forms/create.html"
    success_url = reverse_lazy("home:dashboard")
    extra_context = {
        "title": "Create Server",
        "description": "Create a new server.",
        "form_button_text": "Create Server"
    }
