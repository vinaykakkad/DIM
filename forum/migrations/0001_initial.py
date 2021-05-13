# Generated by Django 3.2.2 on 2021-05-13 03:56

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=300)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos')),
                ('image', models.FileField(blank=True, null=True, upload_to='images')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('tags', models.ManyToManyField(to='forum.Tags')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
