import io
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.core.files import File

from strife.apps.channels.models import Channel
from strife.apps.messages.models import Message


class MessageConsumer(WebsocketConsumer):
    BYTES_SEPARATOR = 33  # ! (exclamation mark)

    # Connection
    def connect(self):
        self.user = self.scope["user"]

        self.server_id = self.scope["url_route"]["kwargs"]["server_id"]
        self.channel_id = self.scope["url_route"]["kwargs"]["channel_id"]
        assert self.server_id
        assert self.channel_id

        self.channel = Channel.objects.get(id=self.channel_id)
        self.server = self.channel.server
        assert self.server.id == self.server_id

        self.channel_group_name = f"chat_{self.channel_id}"

        async_to_sync(self.channel_layer.group_add)(self.channel_group_name, self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.channel_group_name, self.channel_name)

    # Receiving
    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            # Is the data valid?
            text_data_json = json.loads(text_data)
            type = text_data_json["type"]

            supported_types = {"message"}
            if type not in supported_types:
                print("Unsupported type")
                return

            # Dispatch the payload
            if type == "message":
                self.handle_message_payload(text_data_json)
        else:
            # Is the data valid?
            if bytes_data[0] != self.BYTES_SEPARATOR:
                print("Invalid bytes data")
                return

            data_chunks = bytes_data[1:].split(b"!")

            supported_commands = {b"file"}
            if data_chunks[0] not in supported_commands:
                print("Unsupported command")
                return

            # Dispatch the payload
            if data_chunks[0] == b"file":
                self.handle_file_payload(data_chunks)

    def handle_message_payload(self, payload):
        # Are they allowed to send messages?
        if not self.user.as_serverized(self.server.id).can_send_messages:
            return

        # Send the message
        content = payload["content"]
        message = Message.objects.create(
            author=self.user,
            channel_id=self.channel_id,
            content=content,
        )

        # Update websocket clients
        async_to_sync(self.channel_layer.group_send)(
            self.channel_group_name,
            {
                "type": "chat.message",
                "message": message.to_dict(),
            },
        )

    def handle_file_payload(self, payload):
        # Are they allowed to send attachments?
        if not self.user.as_serverized(self.server.id).can_send_attachments:
            return

        # Send the attachment
        metadata = json.loads(payload[1])
        file_obj = payload[2]

        filename = metadata["name"]
        message_id = metadata["messageID"]
        message = Message.objects.get(id=message_id)

        message.attachments.create(
            filename=filename,
            file=File(io.BytesIO(file_obj), name=filename),
        )

        # Update websocket clients
        async_to_sync(self.channel_layer.group_send)(
            self.channel_group_name,
            {
                "type": "chat.attachment",
                "message": message.to_dict(),
            },
        )

    # Sending
    def chat_message(self, event):
        message = event["message"]

        self.send(text_data=json.dumps({"type": "message", "message": message}))

    def chat_attachment(self, event):
        message = event["message"]

        self.send(text_data=json.dumps({"type": "attachment", "message": message}))
