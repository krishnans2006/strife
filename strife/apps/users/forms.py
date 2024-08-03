from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'display_name', 'email', 'password']
