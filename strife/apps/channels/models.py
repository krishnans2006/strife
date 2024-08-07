from django.db import models
from polymorphic.models import PolymorphicModel

from ..servers.models import Server


class Channel(PolymorphicModel):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Channel: {self.name}>"

    class Meta:
        abstract = True
        default_related_name = "channels"


class Messageable(Channel):
    class Meta:
        default_related_name = "messageable_channels"


class TextChannel(Messageable):
    class Meta:
        default_related_name = "text_channels"


class ForumChannel(Messageable):
    class Meta:
        default_related_name = "forum_channels"


class Speakable(Channel):
    class Meta:
        default_related_name = "speakable_channels"


class VoiceChannel(Speakable):
    class Meta:
        default_related_name = "voice_channels"


class StageChannel(Speakable):
    class Meta:
        default_related_name = "stage_channels"
