import os
import random

from django.db import models

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

    # The owner object shouldn't be deleted; only changed
    owner = models.OneToOneField("Owner", on_delete=models.CASCADE)

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

    def __str__(self):
        return self.user.username

    def __repr__(self):
        return f"<Member: {self.user.username}>"


class Owner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner_objs")

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def __repr__(self):
        return f"<Owner: {self.user.username}>"
