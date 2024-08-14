import os
import random

from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.templatetags.static import static
from django.urls import reverse


def user_avatar_path(instance, filename):
    if instance.id:
        return f"avatars/{instance.id}.{filename.split('.')[-1]}"

    random_id = random.randint(100000, 999999)
    while os.path.exists(f"avatars/{random_id}.{filename.split('.')[-1]}"):
        random_id = random.randint(100000, 999999)
    return f"avatars/{random_id}.{filename.split('.')[-1]}"


class User(AbstractUser):
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ("username", "display_name", "password")

    username = models.CharField(max_length=32, unique=True)
    display_name = models.CharField(max_length=32)

    email = models.EmailField(unique=True)

    bio = models.CharField(max_length=2048, blank=True)

    avatar = models.ImageField(upload_to=user_avatar_path, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    @property
    def display_avatar(self):
        if self.avatar:
            return self.avatar.url

        num_avatars = settings.NUM_DEFAULT_AVATARS
        my_avatar = self.id % num_avatars

        return static(f"default-avatars/{my_avatar}.png")

    def get_full_name(self):
        return f"{self.display_name} ({self.username})"

    def get_short_name(self):
        return self.display_name

    # Handle member -> user conversion
    @property
    def is_member(self):
        return False

    def force_user_obj(self):
        return self

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User: {self.username}>"
