from django.db import models

from ..emoji.models import Emoji
from ..messages.models import Message
from ..users.models import User


class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    emoji = models.ForeignKey(Emoji, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.emoji}"

    def __repr__(self):
        return f"<Reaction: {self.user} - {self.emoji}>"
