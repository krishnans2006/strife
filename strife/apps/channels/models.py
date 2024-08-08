from django.db import models
from polymorphic.models import PolymorphicModel

from ..servers.models import Server


class Channel(PolymorphicModel):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    # %(class)ss => channels, messageables, textchannels, etc.
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="%(class)ss")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Channel: {self.name}>"


class Messageable(Channel):
    pass


class TextChannel(Messageable):
    pass


class ForumChannel(Messageable):
    pass


class Speakable(Channel):
    pass


class VoiceChannel(Speakable):
    pass


class StageChannel(Speakable):
    pass
