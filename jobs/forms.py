from django.forms import ModelForm
from django import forms

from .models import JobPost


class JobPostForm(ModelForm):
    class Meta:
        model = JobPost
        fields = ("role", "company", "description", "skills", "location", "salary")
        widgets = {
            "role": forms.TextInput(
                attrs={
                    "class": "form-control fields",
                    "autocomplete": "off",
                    "placeholder": "Role",
                }
            ),
            "company": forms.TextInput(
                attrs={
                    "class": "form-control fields",
                    "autocomplete": "off",
                    "placeholder": "Company",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control fields",
                    "autocomplete": "off",
                    "placeholder": "Description of the job..."
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
            "location": forms.TextInput(
                attrs={
                    "class": "form-control fields",
                    "autocomplete": "off",
                    "placeholder": "Location",
                }
            ),
            "salary": forms.TextInput(
                attrs={
                    "class": "form-control fields",
                    "autocomplete": "off",
                    "placeholder": "Salary",
                }
            ),
        }