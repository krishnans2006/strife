import io
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.core.files import File

from strife.apps.channels.models import Channel
from strife.apps.messages.models import Message


class MessageConsumer(WebsocketConsumer):
    BYTES_SEPARATOR = 33  # ! (exclamation mark)

    def connect(self):
        self.user = self.scope["user"]
        self.channel_id = self.scope["url_route"]["kwargs"]["channel_id"]

        self.channel = Channel.objects.get(id=self.channel_id)
        self.server = self.channel.server

        self.channel_group_name = f"chat_{self.channel_id}"

        async_to_sync(self.channel_layer.group_add)(self.channel_group_name, self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.channel_group_name, self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            # Are they allowed to send messages?
            if not self.user.as_serverized(self.server.id).can_send_messages:
                return

            # Send the message
            text_data_json = json.loads(text_data)
            content = text_data_json["content"]

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

            # Are they trying to send an attachment?
            if data_chunks[0] == b"file":
                # Are they allowed to send attachments?
                if not self.user.as_serverized(self.server.id).can_send_attachments:
                    return

                # Send the attachment
                metadata = json.loads(data_chunks[1])
                file_obj = data_chunks[2]

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

    def chat_message(self, event):
        message = event["message"]

        self.send(text_data=json.dumps({"type": "message", "message": message}))

    def chat_attachment(self, event):
        message = event["message"]

        self.send(text_data=json.dumps({"type": "attachment", "message": message}))
