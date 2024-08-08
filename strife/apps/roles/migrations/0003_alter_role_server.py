# Generated by Django 5.0.7 on 2024-08-08 00:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roles", "0002_initial"),
        ("servers", "0005_alter_member_server_alter_owner_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="role",
            name="server",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="roles",
                to="servers.server",
            ),
        ),
    ]
