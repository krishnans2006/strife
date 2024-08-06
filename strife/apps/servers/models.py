from django.db import models

from ..users.models import User


class Server(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    image = models.ImageField(upload_to="servers/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Server: {self.name}>"


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="member_objs")
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    nickname = models.CharField(max_length=32, blank=True)

    first_joined_at = models.DateTimeField(auto_now_add=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def __repr__(self):
        return f"<Member: {self.user.username}>"


class Owner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    server = models.OneToOneField(Server, on_delete=models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def __repr__(self):
        return f"<Owner: {self.user.username}>"
