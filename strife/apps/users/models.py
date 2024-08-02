from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ("username", "display_name", "password")

    username = models.CharField(max_length=32, unique=True)
    display_name = models.CharField(max_length=32)

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)

    bio = models.CharField(max_length=2048, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_full_name(self):
        return f"{self.display_name} ({self.username})"

    def get_short_name(self):
        return self.display_name

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User: {self.username}>"