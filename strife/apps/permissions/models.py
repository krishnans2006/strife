from django.db import models


class Permissions(models.Model):
    can_manage_server = models.BooleanField(default=False)
    can_manage_roles = models.BooleanField(default=False)
    can_manage_channels = models.BooleanField(default=False)
    can_manage_messages = models.BooleanField(default=False)

    can_send_messages = models.BooleanField(default=False)
    can_send_attachments = models.BooleanField(default=False)

    def __str__(self):
        if self.is_for_server:
            return f"Permissions for server {self.server.name}"
        if self.is_for_role:
            return f"Permissions for role {self.role.name}"
        if self.is_for_member:
            return f"Permissions for member {self.member.username}"
        return "Unassigned permissions object"

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        if sum((self.is_for_server, self.is_for_role, self.is_for_member)) != 1:
            raise ValueError("Permissions object must be assigned to a server, role, or member")
        super().clean()

    # Permissions objects can be assigned to either a server, role, or member
    @property
    def is_for_server(self):
        return hasattr(self, "server")

    @property
    def is_for_role(self):
        return hasattr(self, "role")

    @property
    def is_for_member(self):
        return hasattr(self, "member")

    def __repr__(self):
        return "<Permissions object>"
