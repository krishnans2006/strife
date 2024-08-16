from django.db import models


class Permissions(models.Model):
    can_manage_server = models.BooleanField(default=False)
    can_manage_roles = models.BooleanField(default=False)
    can_manage_channels = models.BooleanField(default=False)
    can_manage_messages = models.BooleanField(default=False)

    can_send_messages = models.BooleanField(default=False)
    can_send_attachments = models.BooleanField(default=False)

    def __str__(self):
        return "Permissions object"

    def __repr__(self):
        return "<Permissions object>"
