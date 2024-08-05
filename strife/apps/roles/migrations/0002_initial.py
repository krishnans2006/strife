# Generated by Django 5.0.7 on 2024-08-05 00:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("roles", "0001_initial"),
        ("servers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="role",
            name="members",
            field=models.ManyToManyField(related_name="roles", to="servers.member"),
        ),
        migrations.AddField(
            model_name="role",
            name="server",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="servers.server"
            ),
        ),
    ]