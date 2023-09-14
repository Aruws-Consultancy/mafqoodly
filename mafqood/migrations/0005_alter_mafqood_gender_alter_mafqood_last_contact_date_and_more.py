# Generated by Django 4.1.3 on 2023-09-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mafqood", "0004_mafqood_reporter_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mafqood",
            name="gender",
            field=models.CharField(
                choices=[("male", "ذكر"), ("female", "انثى")],
                max_length=10,
                verbose_name="الجنس",
            ),
        ),
        migrations.AlterField(
            model_name="mafqood",
            name="last_contact_date",
            field=models.DateTimeField(verbose_name="تاريخ الاختفاء"),
        ),
        migrations.AlterField(
            model_name="mafqood",
            name="name",
            field=models.CharField(max_length=255, verbose_name="الاسم"),
        ),
        migrations.AlterField(
            model_name="mafqood",
            name="surname",
            field=models.CharField(max_length=255, verbose_name="اللقب"),
        ),
    ]
