from django.db import models

from ..users.models import User


def server_image_path(instance, filename):
    return f"servers/{instance.id}.{filename.split('.')[-1]}"


class Server(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    image = models.ImageField(upload_to=server_image_path, blank=True, null=True)

    # The owner object shouldn't be deleted; only changed
    owner = models.OneToOneField("Owner", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
