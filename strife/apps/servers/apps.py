from django.apps import AppConfig


class ServersConfig(AppConfig):
    name = "strife.apps.servers"
    label = "servers"
    verbose_name = "Servers"

    def ready(self):
        from . import signals
