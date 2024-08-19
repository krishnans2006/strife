import io
import json

from asgiref.sync import async_to_sync
from django.core.files import File

from strife.apps.messages.models import Message
from strife.apps.servers.consumers import ServerConsumer


class MessageConsumer(ServerConsumer):
    def initialize(self):
        super().initialize()

        # Set parameters
        self.channel_id = self.scope["url_route"]["kwargs"]["channel_id"]
        assert self.channel_id

        self.channel = self.server.channels.get(id=self.channel_id)
        assert self.channel.id == self.channel_id

        # Register supported types
        self.supported_types_json["message"] = self.handle_message_payload

        # Set group name
        self.group_name = f"chat_{self.channel_id}"

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
            self.group_name,
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

    def chat_message(self, event):
        message = event["message"]

        self.send(text_data=json.dumps({"type": "message", "error": False, "message": message}))

    # Triggered from views.py
    def chat_attachment(self, event):
        message = event["message"]

        self.send(text_data=json.dumps({"type": "attachment", "error": False, "message": message}))
