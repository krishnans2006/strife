# Generated by Django 5.0.7 on 2024-08-05 21:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("servers", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="first_joined_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="server",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
