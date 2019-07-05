from django import forms
from simplemathcaptcha.fields import MathCaptchaField
from simplemathcaptcha.widgets import MathCaptchaWidget


class CaptchaForm(forms.Form):
    captcha = MathCaptchaField(widget=MathCaptchaWidget(question_tmpl='%(num1)i %(operator)s %(num2)i = '))


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=1, widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input', 'type': 'email'}))
    message = forms.CharField(min_length=1, widget=forms.Textarea(attrs={'class': 'textarea'}))
    captcha = MathCaptchaField(widget=MathCaptchaWidget(question_tmpl='%(num1)i %(operator)s %(num2)i = '))
