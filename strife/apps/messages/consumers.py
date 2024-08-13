import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from strife.apps.messages.models import Message


class MessageConsumer(WebsocketConsumer):
    def connect(self):
        self.channel_id = self.scope["url_route"]["kwargs"]["channel_id"]
        self.user = self.scope["user"]

        self.channel_group_name = f"chat_{self.channel_id}"

        async_to_sync(self.channel_layer.group_add)(self.channel_group_name, self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.channel_group_name, self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            text_data_json = json.loads(text_data)
            content = text_data_json["content"]

            message = Message.objects.create(
                author=self.user,
                channel_id=self.channel_id,
                content=content,
            )

            async_to_sync(self.channel_layer.group_send)(
                self.channel_group_name,
                {
                    "type": "chat.message",
                    "message": message.to_dict(),
                },
            )
        else:
            if bytes_data[0] != 33:  # ! (exclamation mark)
                print("Invalid bytes data")
                return

            data_chunks = bytes_data[1:].split(b"!")

            supported_commands = {b"file"}
            if data_chunks[0] not in supported_commands:
                print("Unsupported command")
                return

            if data_chunks[0] == b"file":
                metadata = json.loads(data_chunks[1])
                file_obj = data_chunks[2]
                print(metadata)
                print(file_obj)

    def chat_message(self, event):
        message = event["message"]

        self.send(text_data=json.dumps({"message": message}))
