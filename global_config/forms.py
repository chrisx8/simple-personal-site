from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from global_config.models import EmailConfig


class AuthFormCaptcha(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(min_length=1, widget=forms.PasswordInput(attrs={'class': 'input'}))
    captcha = CaptchaField()


class EmailConfigAdminForm(ModelForm):
    class Meta:
        model = EmailConfig
        exclude = []
        widgets = {'password': forms.PasswordInput}
