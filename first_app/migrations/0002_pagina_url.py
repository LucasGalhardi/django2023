# Generated by Django 4.2.4 on 2023-08-08 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("first_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pagina",
            name="url",
            field=models.URLField(default=None, unique=True),
        ),
    ]
