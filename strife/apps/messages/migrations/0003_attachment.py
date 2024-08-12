# Generated by Django 5.0.7 on 2024-08-12 05:09

import django.db.models.deletion
import strife.apps.messages.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_messages", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attachment",
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
                (
                    "file",
                    models.FileField(
                        upload_to=strife.apps.messages.models.message_attachment_path
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attachments",
                        to="app_messages.message",
                    ),
                ),
            ],
        ),
    ]