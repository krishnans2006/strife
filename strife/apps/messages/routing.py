from django.urls import path

from . import consumers


websocket_urlpatterns = [
    path("ws/messages/", consumers.MessageConsumer.as_asgi()),
]
