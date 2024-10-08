# Generated by Django 5.0.7 on 2024-08-15 04:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_servers", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="server",
            name="owner",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="owned_server",
                to="app_servers.member",
            ),
        ),
    ]
