from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    clinic_name = forms.CharField(help_text='Required.')
    address = forms.CharField(help_text='Required.')
    phone_number = forms.CharField(help_text='Required.')

    class Meta:
        model = User
        fields = ('clinic_name', 'username', 'password1', 'password2', 'address', 'phone_number')
