# Generated by Django 5.0.7 on 2024-08-16 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_permissions", "0001_initial"),
        ("app_servers", "0003_alter_server_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="permissions",
            field=models.OneToOneField(
                default=-1,
                on_delete=django.db.models.deletion.CASCADE,
                to="app_permissions.permissions",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="server",
            name="permissions",
            field=models.OneToOneField(
                default=-1,
                on_delete=django.db.models.deletion.CASCADE,
                to="app_permissions.permissions",
            ),
            preserve_default=False,
        ),
    ]
