from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
