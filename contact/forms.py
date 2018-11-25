from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=1)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, min_length=1)
    captcha = ReCaptchaField()
