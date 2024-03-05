# Generated by Django 5.0.2 on 2024-02-14 06:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("toolapp", "0004_review"),
    ]

    operations = [
        migrations.CreateModel(
            name="contact",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=50)),
                ("phone", models.CharField(max_length=20)),
                ("message", models.TextField(max_length=500)),
            ],
        ),
    ]
