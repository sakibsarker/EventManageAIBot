# Generated by Django 5.1.3 on 2024-11-20 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                choices=[
                    ("ADMIN", "Admin"),
                    ("SELLER", "Seller"),
                    ("BUYER", "Buyer"),
                    ("USER", "User"),
                ],
                default="USER",
                max_length=20,
            ),
        ),
    ]
