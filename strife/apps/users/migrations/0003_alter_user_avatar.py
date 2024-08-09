# Generated by Django 5.0.7 on 2024-08-09 05:14

import strife.apps.users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=strife.apps.users.models.user_avatar_path,
            ),
        ),
    ]