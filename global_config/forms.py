from django import forms
from django.contrib.auth.forms import AuthenticationForm


class AuthFormCaptcha(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(min_length=1, widget=forms.PasswordInput(attrs={'class': 'input'}))
