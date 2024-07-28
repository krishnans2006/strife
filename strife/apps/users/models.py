from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32)
    display_name = models.CharField(max_length=32)

    email = models.EmailField()
    password = models.CharField(max_length=64)

    bio = models.CharField(max_length=2048, blank=True)

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User: {self.username}>"
