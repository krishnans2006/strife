# Generated by Django 5.0.7 on 2024-08-08 01:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("channels", "0001_initial"),
        ("servers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="channel",
            name="server",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)ss",
                to="servers.server",
            ),
        ),
        migrations.CreateModel(
            name="ForumChannel",
            fields=[
                (
                    "messageable_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="channels.messageable",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("channels.messageable",),
        ),
        migrations.CreateModel(
            name="TextChannel",
            fields=[
                (
                    "messageable_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="channels.messageable",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("channels.messageable",),
        ),
        migrations.CreateModel(
            name="StageChannel",
            fields=[
                (
                    "speakable_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="channels.speakable",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("channels.speakable",),
        ),
        migrations.CreateModel(
            name="VoiceChannel",
            fields=[
                (
                    "speakable_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="channels.speakable",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("channels.speakable",),
        ),
    ]
