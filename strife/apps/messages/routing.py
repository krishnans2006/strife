from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(
        "ws/messages/<int:server_id>/<int:channel_id>/",
        consumers.MessageConsumer.as_asgi(),
    ),
]
