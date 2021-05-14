from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm
from django import forms


class Tags(models.Model):
    tag = models.CharField(max_length=220)

    def __str__(self):
        return self.tag


class Post(models.Model):

    title = models.CharField(max_length=256, blank=False)
    description = models.CharField(max_length=300, blank=False)
    text = RichTextUploadingField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, max_length=200, unique=True)
    tags = models.ManyToManyField(Tags)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


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
