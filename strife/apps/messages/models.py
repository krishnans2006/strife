from django.db import models

from strife.apps.channels.models import Messageable
from strife.apps.users.models import User


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")

    channel = models.ForeignKey(Messageable, on_delete=models.CASCADE, related_name="messages")

    content = models.CharField(max_length=2048)

    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    @property
    def is_edited(self):
        return self.edited_at != self.created_at

    def to_dict(self):
        return {
            "id": self.id,
            "author": {
                "id": self.author.id,
                "username": self.author.username,
                "display_avatar": self.author.display_avatar,
            },
            "content": self.content,
            "created_at": self.created_at.isoformat(),
            "edited_at": self.edited_at.isoformat(),
            "is_edited": self.is_edited,
        }

    def __str__(self):
        return f"{self.author} - {self.content[:32]}"

    def __repr__(self):
        return f"<Message: {self.author} - {self.content[:32]}>"
