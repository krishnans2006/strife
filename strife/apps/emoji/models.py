from django.db import models


class Emoji(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Emoji: {self.name}>"
