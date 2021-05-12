from django import forms

from .models import ACCOUNT_TYPES


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control fields', 'autocomplete': 'off',
               'placeholder': 'Username'}
    ))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control fields', 'autocomplete': 'off', 'placeholder': 'Email'}
    ))
    fullname = forms.CharField(label='Fullname', widget=forms.TextInput(
        attrs={'class': 'form-control fields', 'autocomplete': 'off',
               'placeholder': 'Fullname'}
    ))
    type = forms.ChoiceField(label='Choose your account type*',
        choices=ACCOUNT_TYPES, widget=forms.Select(attrs={
        'class': 'form-control fields field-select', 'autocomplete': 'off',
        'placeholder': 'Choose your account type'}
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control fields', 'autocomplete': 'off', 'id': 'password',
               'placeholder': 'Password'}
    ))

    class meta:
        fields = ['username', 'email', 'type', 'password', 'fullname']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control fields', 'autocomplete': 'off',
               'placeholder': 'Username'}
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control fields', 'autocomplete': 'off', 'id': 'password',
               'placeholder': 'Password'}
    ))

    class meta:
        fields = ['username', 'email']