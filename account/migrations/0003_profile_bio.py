# Generated by Django 3.2.2 on 2021-05-14 16:28

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_auto_20210514_2111"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="bio",
            field=ckeditor_uploader.fields.RichTextUploadingField(default="a"),
            preserve_default=False,
        ),
    ]
