from django.core.exceptions import ValidationError
from django.db import models


class Permissions(models.Model):
    can_manage_server = models.BooleanField(default=False)
    can_manage_roles = models.BooleanField(default=False)
    can_manage_channels = models.BooleanField(default=False)
    can_manage_messages = models.BooleanField(default=False)

    can_send_messages = models.BooleanField(default=False)
    can_send_attachments = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Permissions"

    def __str__(self):
        if self.is_for_server:
            return f"Permissions for server {self.server.name}"
        if self.is_for_role:
            return f"Permissions for server {self.role.server.name}, role {self.role.name}"
        if self.is_for_member:
            return f"Permissions for server {self.member.server.name}, member {self.member.user.username}"
        return "Unassigned permissions object"

    def clean(self):
        if sum((self.is_for_server, self.is_for_role, self.is_for_member)) != 1:
            raise ValidationError(
                "Permissions object must be assigned to a server, role, or member"
            )

    def is_valid(self):
        try:
            self.clean()
            return True
        except ValidationError:
            return False

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

    # Initializers
    def set_as_owner(self):
        self.can_manage_server = True
        self.can_manage_roles = True
        self.can_manage_channels = True
        self.can_manage_messages = True

        self.can_send_messages = True
        self.can_send_attachments = True

    # Serialization
    def to_dict(self):
        return {
            "can_manage_server": self.can_manage_server,
            "can_manage_roles": self.can_manage_roles,
            "can_manage_channels": self.can_manage_channels,
            "can_manage_messages": self.can_manage_messages,
            "can_send_messages": self.can_send_messages,
            "can_send_attachments": self.can_send_attachments,
        }

    def __repr__(self):
        return "<Permissions object>"
