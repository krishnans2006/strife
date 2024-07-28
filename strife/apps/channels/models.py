from django.db import models
from polymorphic.models import PolymorphicModel

from apps.servers.models import Server


class Channel(PolymorphicModel):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Channel: {self.name}>"

    class Meta:
        abstract = True


class MessageableChannel(Channel):
    pass


class TextChannel(MessageableChannel):
    pass


class ForumChannel(MessageableChannel):
    pass


class VoiceChannel(Channel):
    raise NotImplementedError


class StageChannel(Channel):
    raise NotImplementedError
