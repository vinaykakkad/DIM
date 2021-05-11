# Generated by Django 3.2.2 on 2021-05-11 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=220, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('fullname', models.CharField(blank=True, max_length=220, null=True)),
                ('type', models.CharField(choices=[('recruiter', 'recruiter'), ('expert', 'expert'), ('user', 'user')], max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_activated', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
