from django.db import models
from django.urls import reverse

from ..servers.models import Server, Member


class Role(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    color = models.CharField(max_length=6)  # hex

    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="roles")

    members = models.ManyToManyField(Member, related_name="roles")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("servers:roles:edit", kwargs={"server_id": self.server.id, "role_id": self.id})

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Role: {self.name}>"
