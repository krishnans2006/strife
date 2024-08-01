from django.db import models

from apps.users.models import User


class Server(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Server: {self.name}>"


class Member(User):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<Member: {self.username}>"
