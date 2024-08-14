import os
import random

from django.db import models
from django.urls import reverse

from strife.apps.servers.models import Member
from strife.apps.channels.models import Messageable
from strife.apps.users.models import User


def message_attachment_path(instance, filename):
    if instance.id:
        return f"attachments/{instance.id}.{filename.split('.')[-1]}"

    random_id = random.randint(100000, 999999)
    while os.path.exists(f"attachments/{random_id}.{filename.split('.')[-1]}"):
        random_id = random.randint(100000, 999999)
    return f"attachments/{random_id}.{filename.split('.')[-1]}"


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")

    channel = models.ForeignKey(Messageable, on_delete=models.CASCADE, related_name="messages")

    content = models.CharField(max_length=2048)

    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    @property
    def is_edited(self):
        return self.edited_at != self.created_at

    @property
    def member(self):
        return Member.objects.get(user=self.author, server=self.channel.server)

    def to_dict(self):
        return {
            "id": self.id,
            "author": {
                "id": self.author.id,
                "username": self.author.username,
                "display_avatar": self.author.display_avatar,
            },
            "member": {
                "id": self.member.id,
                "nickname": self.member.nickname,
                "roles": [
                    {
                        "id": role.id,
                        "name": role.name,
                        "description": role.description,
                        "color": role.color,
                    }
                    for role in self.member.roles.all()
                ]
            },
            "content": self.content,
            "created_at": self.created_at.isoformat(),
            "edited_at": self.edited_at.isoformat(),
            "is_edited": self.is_edited,
            "attachments": [
                {
                    "id": attachment.id,
                    "name": attachment.filename,
                    "url": attachment.url,
                    "view_url": attachment.view_url,
                    "download_url": attachment.download_url,
                }
                for attachment in self.attachments.all()
            ],
        }

    def __str__(self):
        return f"{self.author} - {self.content[:32]}"

    def __repr__(self):
        return f"<Message: {self.author} - {self.content[:32]}>"


class Attachment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="attachments")

    filename = models.CharField(max_length=256)
    file = models.FileField(upload_to=message_attachment_path)

    #@override
    def save(self, *args, **kwargs):
        if not self.id:
            # Remove file, save, then add file
            # This is to use the attachment ID in the file path
            attachment_file = self.file
            self.file = None
            super().save(*args, **kwargs)
            self.file = attachment_file

            # Allow model updates in the same function as creation
            if "force_insert" in kwargs:
                kwargs.pop("force_insert")

        super().save(*args, **kwargs)

    @property
    def name(self):
        return self.filename

    @property
    def url(self):
        return self.file.url

    @property
    def view_url(self):
        kwargs = {
            "server_id": self.message.channel.server.id,
            "channel_id": self.message.channel.id,
            "message_id": self.message.id,
            "attachment_id": self.id,
        }
        return reverse("servers:channels:messages:view_attachment", kwargs=kwargs)

    @property
    def download_url(self):
        kwargs = {
            "server_id": self.message.channel.server.id,
            "channel_id": self.message.channel.id,
            "message_id": self.message.id,
            "attachment_id": self.id,
        }
        return reverse("servers:channels:messages:download_attachment", kwargs=kwargs)

    def __str__(self):
        return f"{self.message} - {self.file.name}"

    def __repr__(self):
        return f"<Attachment: {self.message} - {self.file.name}>"
