from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .models import Channel, TextChannel
from ..servers.models import Server


# This view will not work (Channel is an abstract model)
# It is only here for inheritance purposes
class GenericChannelCreateView(LoginRequiredMixin, CreateView):
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
        server_id = self.kwargs.get("server_id")
        form.instance.server = Server.objects.get(pk=server_id)
        return super().form_valid(form)


class TextChannelCreateView(GenericChannelCreateView):
    model = TextChannel
    extra_context = {
        "title": "Create a Text Channel",
        "description": "***Set by get_context_data() below***",
        "form_button_text": "Create Text Channel"
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        server_id = self.kwargs.get("server_id")
        server = Server.objects.get(pk=server_id)
        context["description"] = f"In {server}."
        return context


class TextChannelDetailView(LoginRequiredMixin, DetailView):
    model = TextChannel
    template_name = "channels/detail.html"
    context_object_name = "channel"
    pk_url_kwarg = "channel_id"
