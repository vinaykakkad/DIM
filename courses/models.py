from django.db import models

# Create your models here.

class fields(models.Model):
    Field = models.CharField(max_length=200)

    def __str__(self):
        return self.Field

class courses(models.Model):
    name = models.CharField(max_length=200, blank=False)
    link = models.CharField(max_length=10000, blank=False)
    price = models.IntegerField()
    Field = models.ManyToManyField(fields)

