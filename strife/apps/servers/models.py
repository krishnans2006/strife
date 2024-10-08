import os
import random

from django.db import models
from django.urls import reverse

from ..permissions.models import Permissions
from ..users.models import User


def server_image_path(instance, filename):
    if instance.id:
        return f"servers/{instance.id}.{filename.split('.')[-1]}"

    random_id = random.randint(100000, 999999)
    while os.path.exists(f"servers/{random_id}.{filename.split('.')[-1]}"):
        random_id = random.randint(100000, 999999)
    return f"servers/{random_id}.{filename.split('.')[-1]}"


class Server(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    image = models.ImageField(upload_to=server_image_path, blank=True, null=True)

    # Must be nullable, as the server is created before the owner
    owner = models.OneToOneField(
        "Member", on_delete=models.PROTECT, related_name="owned_server", null=True
    )

    permissions = models.OneToOneField(Permissions, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # @override
    def save(self, *args, **kwargs):
        if not self.id:
            # Add permissions object
            permissions = Permissions.objects.create()
            self.permissions = permissions
            assert self.permissions.is_valid()

            # Remove image, save, then add image
            # This is to use the server ID in the image path
            server_image = self.image
            self.image = None
            super().save(*args, **kwargs)
            self.image = server_image

            # Allow model updates in the same function as creation
            if "force_insert" in kwargs:
                kwargs.pop("force_insert")

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("servers:detail", kwargs={"server_id": self.id})

    @property
    def channels(self):
        return self.channels.all()

    def __repr__(self):
        return f"<Server: {self.name}>"


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="member_objs")
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="members")

    nickname = models.CharField(max_length=32, blank=True)

    permissions = models.OneToOneField(Permissions, on_delete=models.CASCADE)

    first_joined_at = models.DateTimeField(auto_now_add=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    # @override
    def save(self, *args, **kwargs):
        if not self.id or not hasattr(self, "permissions"):
            # New role, add permissions object
            permissions = Permissions.objects.create()
            self.permissions = permissions
            assert self.permissions.is_valid()

        super().save(*args, **kwargs)

    # Serialization
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user.id,
            "username": self.username,
            "display_name": self.display_name,
            "email": self.email,
            "bio": self.bio,
            "display_avatar": self.display_avatar,
            "is_serverized": self.is_serverized,
            "roles": [role.to_dict() for role in self.roles.all()],
        }

    # Properties for quick access to User
    @property
    def username(self):
        return self.user.username

    @property
    def display_name(self):
        return self.user.display_name

    @property
    def email(self):
        return self.user.email

    @property
    def bio(self):
        return self.user.bio

    @property
    def avatar(self):
        return self.user.avatar

    @property
    def display_avatar(self):
        return self.user.display_avatar

    # Handle member -> user conversion
    @property
    def is_serverized(self):
        return True

    @property
    def as_user(self):
        return self.user

    def as_serverized(self, server_id: int):
        if server_id == self.server.id:
            return self
        return self.user.as_serverized(server_id)

    # Permissions
    @property
    def permissions_dict(self):
        all_permission_objs = [
            self.server.permissions,
            self.permissions,
            *(role.permissions for role in self.roles.all()),
        ]

        return {
            perm: any(getattr(perm_obj, perm) for perm_obj in all_permission_objs)
            for perm in (
                "can_manage_server",
                "can_manage_roles",
                "can_manage_channels",
                "can_manage_messages",
                "can_send_messages",
                "can_send_attachments",
            )
        }

    @property
    def permissions_repr(self):
        all_permission_objs = [
            self.server.permissions,
            self.permissions,
            *(role.permissions for role in self.roles.all()),
        ]

        return "".join(
            "1" if any(getattr(perm_obj, perm) for perm_obj in all_permission_objs) else "0"
            for perm in (
                "can_manage_server",
                "can_manage_roles",
                "can_manage_channels",
                "can_manage_messages",
                "can_send_messages",
                "can_send_attachments",
            )
        )

    @property
    def can_manage_server(self):
        return any(
            (
                self.server.permissions.can_manage_server,
                self.permissions.can_manage_server,
                *(role.permissions.can_manage_server for role in self.roles.all()),
            )
        )

    @property
    def can_manage_roles(self):
        return any(
            (
                self.server.permissions.can_manage_roles,
                self.permissions.can_manage_roles,
                *(role.permissions.can_manage_roles for role in self.roles.all()),
            )
        )

    @property
    def can_manage_channels(self):
        return any(
            (
                self.server.permissions.can_manage_channels,
                self.permissions.can_manage_channels,
                *(role.permissions.can_manage_channels for role in self.roles.all()),
            )
        )

    @property
    def can_manage_messages(self):
        return any(
            (
                self.server.permissions.can_manage_messages,
                self.permissions.can_manage_messages,
                *(role.permissions.can_manage_messages for role in self.roles.all()),
            )
        )

    @property
    def can_send_messages(self):
        return any(
            (
                self.server.permissions.can_send_messages,
                self.permissions.can_send_messages,
                *(role.permissions.can_send_messages for role in self.roles.all()),
            )
        )

    @property
    def can_send_attachments(self):
        return any(
            (
                self.server.permissions.can_send_attachments,
                self.permissions.can_send_attachments,
                *(role.permissions.can_send_attachments for role in self.roles.all()),
            )
        )

    def __repr__(self):
        return f"<Member: {self.user.username}>"
