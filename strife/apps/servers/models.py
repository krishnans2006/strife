import os
import random

from django.db import models

from strife.apps.users.models import User


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

    owner = models.OneToOneField("Member", on_delete=models.PROTECT, related_name="owned_server")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #@override
    def save(self, *args, **kwargs):
        if not self.id:
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

    @property
    def channels(self):
        return self.channels.all()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Server: {self.name}>"


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="member_objs")
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="members")

    nickname = models.CharField(max_length=32, blank=True)

    first_joined_at = models.DateTimeField(auto_now_add=True)
    joined_at = models.DateTimeField(auto_now_add=True)

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

    def __str__(self):
        return self.user.username

    def __repr__(self):
        return f"<Member: {self.user.username}>"
