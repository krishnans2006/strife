from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(
        "ws/<int:server_id>/<int:channel_id>/",
        consumers.MessageConsumer.as_asgi(),
        kwargs={"server_id": None, "channel_id": None},
    ),
]
