from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class GenericConsumer(WebsocketConsumer):
    BYTES_SEPARATOR = 33  # ! (exclamation mark)

    group_name = "default"
    supported_types_json = {}
    supported_types_bytes = {}

    def initialize(self):
        self.supported_types_json["ping"] = self.handle_ping
        # ...more

    def connect(self):
        self.user = self.scope["user"]

        self.initialize()

        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

    def handle_ping(self, payload):
        pass
