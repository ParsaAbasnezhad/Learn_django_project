from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-field', 'style': 'width: 88%', 'border': 'none'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'style': 'width: 88%', 'border': 'none'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("نام کاربری یا رمز عبور اشتباه است.")
        return cleaned_data
