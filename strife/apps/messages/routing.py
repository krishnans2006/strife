from django.urls import path

from . import consumers


websocket_urlpatterns = [
    path(
        "servers/<int:server_id>/channels/<int:channel_id>/messages/ws/",
        consumers.MessageConsumer.as_asgi(),
    ),
]
