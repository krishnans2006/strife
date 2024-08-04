from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from ...utils import StrifeForm
from .models import User


class LoginForm(AuthenticationForm, StrifeForm):
    pass


class RegisterForm(UserCreationForm, StrifeForm):
    class Meta:
        model = User
        fields = ['username', 'display_name', 'email', 'password']
