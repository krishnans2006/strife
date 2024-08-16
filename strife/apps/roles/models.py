from django.db import models
from django.urls import reverse

from ..permissions.models import Permissions
from ..servers.models import Member, Server


class Role(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    color = models.CharField(max_length=6)  # hex

    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="roles")

    members = models.ManyToManyField(Member, related_name="roles")

    permissions = models.OneToOneField(Permissions, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # @override
    def save(self, *args, **kwargs):
        if not self.id or not hasattr(self, "permissions"):
            # New role, add permissions object
            permissions = Permissions.objects.create()
            self.permissions = permissions

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "servers:roles:edit", kwargs={"server_id": self.server.id, "role_id": self.id}
        )

    def __repr__(self):
        return f"<Role: {self.name}>"
