from django.forms import ModelForm
from django import forms

from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("title", "description", "text", "tags")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control fields",
                    "autocomplete": "off",
                    "placeholder": "Title",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control fields",
                    "autocomplete": "off",
                    "placeholder": "Description",
                }
            ),
            "tags": forms.SelectMultiple(
                attrs={
                    "class": "selectpicker fields",
                    "autocomplete": "off",
                    "placeholder": "Tags",
                    "size": "1",
                    "data-live-search": "true",
                }
            ),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
