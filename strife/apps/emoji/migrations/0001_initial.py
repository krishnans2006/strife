# Generated by Django 5.0.7 on 2024-08-01 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Emoji",
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
                ("name", models.CharField(max_length=32)),
                ("description", models.CharField(max_length=256)),
                ("image", models.ImageField(upload_to="emojis")),
            ],
        ),
    ]
