from django.db import models

from apps.servers.models import Server


class Channel(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Channel: {self.name}>"

    class Meta:
        abstract = True


class TextChannel(Channel):
    pass


class ForumChannel(Channel):
    pass


class VoiceChannel(Channel):
    raise NotImplementedError


class StageChannel(Channel):
    raise NotImplementedError
