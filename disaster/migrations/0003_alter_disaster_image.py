# Generated by Django 4.1.3 on 2023-09-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("disaster", "0002_disaster_closed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disaster",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="disasters"),
        ),
    ]
