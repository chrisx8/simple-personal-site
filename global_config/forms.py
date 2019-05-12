from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, Form
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from global_config.models import EmailConfig
from global_config.site_config import RECAPTCHA_PRIVATE_KEY, RECAPTCHA_PUBLIC_KEY


class AuthFormCaptcha(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(min_length=1, widget=forms.PasswordInput(attrs={'class': 'input'}))
    if RECAPTCHA_PRIVATE_KEY and RECAPTCHA_PUBLIC_KEY:
        captcha = ReCaptchaField(widget=ReCaptchaWidget())


class EmailConfigAdminForm(ModelForm):
    class Meta:
        model = EmailConfig
        exclude = []
        widgets = {'password': forms.PasswordInput}


class RecaptchaForm(Form):
    if RECAPTCHA_PRIVATE_KEY and RECAPTCHA_PUBLIC_KEY:
        captcha = ReCaptchaField(widget=ReCaptchaWidget())
