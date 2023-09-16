from django.db import models
from config.constants import Options
from django.core.validators import RegexValidator

onlynumbers = RegexValidator(r'^[0-9]', 'Only numbers are allowed.')


class Volunteer(models.Model):

    name = models.CharField(max_length=255, blank=False, null=False, verbose_name="الاسم")
    surname = models.CharField(max_length=255, blank=False, null=False, verbose_name="اللقب")

    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="عنوان السكن")
    city = models.CharField(max_length=255, blank=False, null=False, verbose_name="المدينة")
    gender = models.CharField(max_length=10, null=False, blank=False, choices=Options.general['gender'], verbose_name="الجنس")

    contact_number = models.CharField(max_length=14, blank=False, null=False, validators=[onlynumbers], verbose_name="رقم الهاتف")
    email_address = models.CharField(max_length=255, blank=False, null=False, verbose_name="البريد الالكتروني")

    about_volunteer = models.TextField(max_length=255, blank=True, null=True, verbose_name="نبذة عن المتطوع")

    photograph = models.ImageField(upload_to='mafqood', blank=True, null=True, verbose_name="صورة")

    status = models.CharField(max_length=50, null=True, blank=True, default="new", choices=Options.volunteer['status'])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'
