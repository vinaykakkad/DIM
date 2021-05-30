from django.db import models
from django.db.models.base import ModelState

# Create your models here.

class fields(models.Model):
    Field = models.CharField(max_length=200)

    def __str__(self):
        return self.Field

class courses(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    posted_on = models.DateTimeField(auto_now=True)
    link = models.URLField(max_length=10000, blank=False)
    price = models.IntegerField()
    Field = models.ManyToManyField(fields, related_name='fields')

