from django.db import models

from apps.channels.models import MessageableChannel
from apps.users.models import User


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    channel = models.ForeignKey(MessageableChannel, on_delete=models.CASCADE)

    content = models.CharField(max_length=2048)

    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    @property
    def is_edited(self):
        return self.edited_at != self.created_at

    def __str__(self):
        return f"{self.author} - {self.content[:32]}"

    def __repr__(self):
        return f"<Message: {self.author} - {self.content[:32]}>"
