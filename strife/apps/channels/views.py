from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Channel
from ..servers.models import Server


class ChannelCreateView(CreateView, LoginRequiredMixin):
    model = Channel
    fields = ("name", "description")
    template_name = "forms/create.html"
    success_url = reverse_lazy("home:dashboard")
    extra_context = {
        "title": "Create Server",
        "description": "Create a new server.",
        "form_button_text": "Create Server"
    }

    def form_valid(self, form):
        server_id = super().get_form_kwargs().get("server_id")
        form.instance.server = Server.objects.get(pk=server_id)
