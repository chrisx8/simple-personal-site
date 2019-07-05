from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from simplemathcaptcha.fields import MathCaptchaField
from simplemathcaptcha.widgets import MathCaptchaWidget
from global_config.models import EmailConfig


class AuthFormCaptcha(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(min_length=1, widget=forms.PasswordInput(attrs={'class': 'input'}))
    captcha = MathCaptchaField(widget=MathCaptchaWidget(question_tmpl='%(num1)i %(operator)s %(num2)i = '))


class EmailConfigAdminForm(ModelForm):
    class Meta:
        model = EmailConfig
        exclude = []
        widgets = {'password': forms.PasswordInput}
