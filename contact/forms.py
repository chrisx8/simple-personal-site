from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=1, widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input'}))
    message = forms.CharField(min_length=1, widget=forms.Textarea(attrs={'class': 'textarea'}))
    captcha = ReCaptchaField()
