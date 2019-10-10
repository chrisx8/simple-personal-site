from django import forms
from django.conf import settings
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class CaptchaForm(forms.Form):
    if settings.RECAPTCHA_PRIVATE_KEY and settings.RECAPTCHA_PUBLIC_KEY:
        captcha = ReCaptchaField(widget=ReCaptchaWidget())


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=1, widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input', 'type': 'email'}))
    message = forms.CharField(min_length=1, widget=forms.Textarea(attrs={'class': 'textarea'}))
    if settings.RECAPTCHA_PRIVATE_KEY and settings.RECAPTCHA_PUBLIC_KEY:
        captcha = ReCaptchaField(widget=ReCaptchaWidget())
