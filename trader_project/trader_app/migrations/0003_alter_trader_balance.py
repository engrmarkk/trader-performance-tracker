# Generated by Django 4.2.1 on 2023-05-22 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trader_app", "0002_remove_trader_email_remove_trader_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trader",
            name="balance",
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=10),
        ),
    ]
