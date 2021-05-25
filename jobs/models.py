from django.db import models
from account.models import Account, Skill


class JobPost(models.Model):
    role = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    description = models.TextField()
    recruiter = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="job_posts"
    )
    posted_on = models.DateTimeField(auto_now=True)
    skills = models.ManyToManyField(Skill)
    location = models.CharField(max_length=300)
    salary = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.role}@{self.company}_{self.pk}"
