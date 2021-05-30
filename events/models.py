from django.db import models
from account.models import Account, Skill


class EventPost(models.Model):
    title = models.CharField(max_length=300)
    organization = models.CharField(max_length=300)
    description = models.TextField()
    posted_by = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="event_posts"
    )
    posted_on = models.DateTimeField(auto_now=True)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f"{self.title}_{self.pk}"
