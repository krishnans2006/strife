from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView

from ..servers.models import Server
from .models import Channel, TextChannel


# This view will not work (Channel is an abstract model)
# It is only here for inheritance purposes
class GenericChannelCreateView(LoginRequiredMixin, CreateView):
    model = Channel
    fields = ("name", "description")
    template_name = "forms/page.html"
    extra_context = {
        "title": "Create Server",
        "description": "Create a new server.",
        "form_button_text": "Create Server",
    }

    def get_success_url(self):
        return self.object.server.get_absolute_url()

    def form_valid(self, form):
        server_id = self.kwargs.get("server_id")
        form.instance.server = Server.objects.get(pk=server_id)
        return super().form_valid(form)


class TextChannelCreateView(GenericChannelCreateView):
    model = TextChannel
    extra_context = {
        "title": "Create a Text Channel",
        "description": "***Set by get_context_data() below***",
        "form_button_text": "Create Text Channel",
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
    extra_context = {
        "server": "***Set by get_context_data() below***",
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["server"] = self.object.server
        context["member"] = self.request.user.as_serverized(context["server"].id)
        return context
