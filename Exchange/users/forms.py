from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import User
from .models import Profile
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']


class DepositForm(forms.Form):
    card_number = forms.NumberInput()
    card_month_expired = forms.NumberInput()
    card_year_expired = forms.NumberInput()
    card_ccv = forms.NumberInput()
    name = forms.CharField()
    amount = forms.NumberInput()
