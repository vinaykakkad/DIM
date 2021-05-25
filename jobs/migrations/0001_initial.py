# Generated by Django 3.2.2 on 2021-05-25 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="JobPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("role", models.CharField(max_length=300)),
                ("company", models.CharField(max_length=300)),
                ("description", models.TextField()),
                ("posted_on", models.DateTimeField(auto_now=True)),
                ("location", models.CharField(max_length=300)),
                ("salary", models.CharField(max_length=300)),
                (
                    "recruiter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("skills", models.ManyToManyField(to="account.Skill")),
            ],
        ),
    ]
