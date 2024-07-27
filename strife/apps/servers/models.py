from django.db import models


class Server(models.Model):
    # This model represents a discord server.
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=4096)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Server: {self.name}>"
