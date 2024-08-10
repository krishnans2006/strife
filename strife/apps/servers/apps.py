from django.apps import AppConfig


class ServersConfig(AppConfig):
    name = "strife.apps.servers"
    label = "app_servers"
    verbose_name = "Servers"

    def ready(self):
        from . import signals
