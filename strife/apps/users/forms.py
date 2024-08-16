from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from ...utils import StrifeForm
from .models import User


class LoginForm(AuthenticationForm, StrifeForm):
    pass


class RegisterForm(UserCreationForm, StrifeForm):
    class Meta:
        model = User
        fields = ["username", "display_name", "email"]


class UpdateProfileForm(UserChangeForm, StrifeForm):
    class Meta:
        model = User
        fields = ["display_name", "avatar"]
