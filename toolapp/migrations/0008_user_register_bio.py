# Generated by Django 5.0.2 on 2024-02-21 04:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("toolapp", "0007_user_register_address_user_register_age_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_register",
            name="bio",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]