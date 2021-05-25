from django import forms
from django.forms import widgets

from .models import ACCOUNT_TYPES, Profile


class RegisterForm(forms.Form):
    """
    Account Registration Form
        - Adding accounts
        - Updating accounts
    """

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": "form-control fields",
                "autocomplete": "off",
                "placeholder": "Username",
            }
        ),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control fields",
                "autocomplete": "off",
                "placeholder": "Email",
            }
        ),
    )
    fullname = forms.CharField(
        label="Fullname",
        widget=forms.TextInput(
            attrs={
                "class": "form-control fields",
                "autocomplete": "off",
                "placeholder": "Fullname",
            }
        ),
    )
    type = forms.ChoiceField(
        label="Choose your account type*",
        choices=ACCOUNT_TYPES,
        widget=forms.Select(
            attrs={
                "class": "form-control fields field-select",
                "autocomplete": "off",
                "placeholder": "Choose your account type",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control fields",
                "autocomplete": "off",
                "id": "password",
                "placeholder": "Password",
            }
        ),
    )

    class meta:
        fields = ["username", "email", "type", "password", "fullname"]


class LoginForm(forms.Form):
    """
    Account Registration Form
        - Authenticate User
    """

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": "form-control fields",
                "autocomplete": "off",
                "placeholder": "Username",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control fields",
                "autocomplete": "off",
                "id": "password",
                "placeholder": "Password",
            }
        ),
    )

    class meta:
        fields = ["username", "email"]


class ProfileForm(forms.ModelForm):
    """
    Account Registration Form
        - Adding profile
        - Updating profile
    """

    class Meta:
        model = Profile
        fields = ("linkedin_url", "github_url", "bio", "skills")
        widgets = {
            "linkedin_url": forms.URLInput(
                attrs={
                    "class": "form-control fields",
                    "autocomplete": "off",
                    "placeholder": "Linkedin URL",
                }
            ),
            "github_url": forms.TextInput(
                attrs={
                    "class": "form-control fields",
                    "autocomplete": "off",
                    "placeholder": "Github URL",
                }
            ),
            "skills": forms.SelectMultiple(
                attrs={
                    "class": "selectpicker fields",
                    "autocomplete": "off",
                    "placeholder": "Skills",
                    "size": "1",
                    "data-live-search": "true",
                    "data-max-options": "5",
                }
            ),
        }
