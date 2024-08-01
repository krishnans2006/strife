from django.db import models

from ..emoji.models import Emoji
from ..messages.models import Message
from ..users.models import User


class Reaction(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    emoji = models.ForeignKey(Emoji, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Reaction: {self.name}>"
