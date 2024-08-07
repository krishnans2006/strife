from django.db import models
from polymorphic.models import PolymorphicModel

from ..servers.models import Server


class Channel(PolymorphicModel):
    @staticmethod
    def get_channels_related_name():
        return "channels"

    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name=get_channels_related_name.__func__())

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Channel: {self.name}>"

    class Meta:
        abstract = True


class Messageable(Channel):
    @staticmethod
    def get_channels_related_name():
        return "messageable_channels"


class TextChannel(Messageable):
    @staticmethod
    def get_channels_related_name():
        return "text_channels"


class ForumChannel(Messageable):
    @staticmethod
    def get_channels_related_name():
        return "forum_channels"


class Speakable(Channel):
    @staticmethod
    def get_channels_related_name():
        return "speakable_channels"


class VoiceChannel(Speakable):
    @staticmethod
    def get_channels_related_name():
        return "voice_channels"


class StageChannel(Speakable):
    @staticmethod
    def get_channels_related_name():
        return "stage_channels"
