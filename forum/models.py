from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from account.models import Account


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
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="posts")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = RichTextUploadingField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.post}_{self.user}_{self.pk}"
