from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from global_config.site_config import RECAPTCHA_PUBLIC_KEY, RECAPTCHA_PRIVATE_KEY


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=1, widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input', 'type': 'email'}))
    message = forms.CharField(min_length=1, widget=forms.Textarea(attrs={'class': 'textarea'}))
    if RECAPTCHA_PUBLIC_KEY and RECAPTCHA_PRIVATE_KEY:
        captcha = ReCaptchaField(widget=ReCaptchaWidget())
