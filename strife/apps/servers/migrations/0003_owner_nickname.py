# Generated by Django 5.0.7 on 2024-08-15 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_servers", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="owner",
            name="nickname",
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
