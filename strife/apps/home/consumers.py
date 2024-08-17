import json

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

    # Receiving
    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            # Is the data valid?
            text_data_json = json.loads(text_data)
            type = text_data_json["type"]

            if type not in self.supported_types_json:
                print("Unsupported type")
                return

            # Dispatch the payload
            self.supported_types_json[type](text_data_json)
        else:
            # Is the data valid?
            if bytes_data[0] != self.BYTES_SEPARATOR:
                print("Invalid bytes data")
                return

            data_chunks = bytes_data[1:].split(b"!")

            if data_chunks[0] not in self.supported_types_bytes:
                print("Unsupported command")
                return

            # Dispatch the payload
            self.supported_types_bytes[data_chunks[0]](data_chunks)

    def handle_ping(self, payload):
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                "type": "ping",
                "message": "pong",
            },
        )

    def ping(self, event):
        self.send(text_data=json.dumps(event))