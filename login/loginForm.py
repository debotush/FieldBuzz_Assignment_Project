from django import forms
from .models import LoginModel


class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        labels = {
            'username': 'Username',
            'password': 'Password'
        }
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ('username', 'password')
