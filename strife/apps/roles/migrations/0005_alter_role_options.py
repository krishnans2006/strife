# Generated by Django 5.0.7 on 2024-08-20 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_roles", "0004_alter_role_members"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="role",
            options={"ordering": ("name",)},
        ),
    ]
