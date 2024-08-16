from django import forms

from .models import Permissions


class PermissionsForm(forms.ModelForm):
    class Meta:
        model = Permissions
        fields = (
            "can_manage_server",
            "can_manage_roles",
            "can_manage_channels",
            "can_manage_messages",
            "can_send_messages",
            "can_send_attachments",
        )
