from django.db import models

from ..servers.models import Server, Member


class Role(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    color = models.CharField(max_length=6)  # hex

    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    members = models.ManyToManyField(Member, related_name="roles")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Role: {self.name}>"
