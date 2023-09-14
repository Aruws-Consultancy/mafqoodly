# Generated by Django 4.1.3 on 2023-09-14 06:47

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("mafqood", "0002_remove_mafqood_last_contact_details_mafqood_clothing"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mafqood",
            name="contact_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                max_length=128,
                null=True,
                region=None,
                verbose_name="رقم الهاتف",
            ),
        ),
        migrations.AlterField(
            model_name="mafqood",
            name="reporter_contact_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                max_length=128,
                null=True,
                region=None,
                verbose_name="رقم الهاتف",
            ),
        ),
        migrations.AlterField(
            model_name="mafqood",
            name="reporter_contact_number_2",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                max_length=128,
                null=True,
                region=None,
                verbose_name="رقم الهاتف 2",
            ),
        ),
        migrations.AlterField(
            model_name="mafqood",
            name="reporter_relation_to_missing",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="صلة القرابة للمفقود",
            ),
        ),
    ]