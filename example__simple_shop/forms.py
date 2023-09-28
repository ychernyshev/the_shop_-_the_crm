from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form.control right-angle w-100',
        'placeholder': 'Username'
    }))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'form.control right-angle w-100',
        'placeholder': 'Ender the password'
    }))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'form.control right-angle w-100',
        'placeholder': 'Confirm the password'
    }))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form.control right-angle w-100',
        'placeholder': 'Username'
    }))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'form.control right-angle w-100',
        'placeholder': 'Ender the password'
    }))