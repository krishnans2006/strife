from django import forms

from .models import Role


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ("name", "description", "color")
