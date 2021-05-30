from django.forms import ModelForm
from django import forms

from .models import EventPost


class EventPostForm(ModelForm):
    class Meta:
        model = EventPost
        fields = ("title", "organization", "description", "skills")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control fields",
                    "autocomplete": "off",
                    "placeholder": "Title",
                }
            ),
            "organization": forms.TextInput(
                attrs={
                    "class": "form-control fields",
                    "autocomplete": "off",
                    "placeholder": "Organization",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control fields",
                    "autocomplete": "off",
                    "placeholder": "Description of the event...",
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
