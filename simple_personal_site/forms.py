from django import forms
from django.contrib.auth.forms import AuthenticationForm
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class AuthFormCaptcha(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(min_length=1, widget=forms.PasswordInput(attrs={'class': 'input'}))
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
