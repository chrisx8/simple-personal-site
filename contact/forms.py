from django import forms
from django.conf import settings


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=1, widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input', 'type': 'email'}))
    message = forms.CharField(min_length=1, widget=forms.Textarea(attrs={'class': 'textarea'}))
    # honeypot
    url = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'contacturl'}))
