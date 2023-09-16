from django.db import models
from config.constants import Options
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

onlynumbers = RegexValidator(r'^[0-9]', 'Only numbers are allowed.')


class Team(models.Model):

    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)

    status = models.CharField(max_length=50, null=True, blank=True, default="new", choices=Options.volunteer['status'])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Volunteer(models.Model):

    name = models.CharField(max_length=255, blank=False, null=False, verbose_name="الاسم")
    surname = models.CharField(max_length=255, blank=False, null=False, verbose_name="اللقب")

    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="عنوان السكن")
    city = models.CharField(max_length=255, blank=False, null=False, verbose_name="المدينة")
    gender = models.CharField(max_length=10, null=False, blank=False, choices=Options.general['gender'], verbose_name="الجنس")

    contact_number = models.CharField(max_length=14, blank=False, null=False, validators=[onlynumbers], verbose_name="رقم الهاتف")
    email_address = models.CharField(max_length=255, blank=False, null=False, verbose_name="البريد الالكتروني")

    about_volunteer = models.TextField(max_length=255, blank=True, null=True, verbose_name="نبذة عن المتطوع")

    photograph = models.ImageField(upload_to='volunteer', blank=True, null=True, verbose_name="صورة المتطوع")

    status = models.CharField(max_length=50, null=True, blank=True, default="new", choices=Options.volunteer['status'])
    created = models.DateTimeField(auto_now_add=True)

    assigned_team = models.ForeignKey(Team, related_name='volunteers', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="فريق العمل")

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    @property
    def is_current_user(self):
        matched_users = User.objects.filter(email=self.email_address)
        if matched_users.count() > 0:
            return matched_users.first()
        return None

