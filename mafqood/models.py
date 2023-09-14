from django.db import models
from datetime import date, timedelta
from config.constants import Options
from disaster.models import Disaster
from django.core.validators import RegexValidator

onlynumbers = RegexValidator(r'^[0-9]', 'Only numbers are allowed.')

class Mafqood(models.Model):

    disaster = models.ForeignKey(Disaster, related_name='missings', null=False, blank=False, on_delete=models.CASCADE)

    # Missing Person
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name="الاسم")
    surname = models.CharField(max_length=255, blank=False, null=False, verbose_name="اللقب")

    date_of_birth = models.DateField(blank=True, null=True, verbose_name="تاريخ الميلاد")
    age = models.IntegerField(blank=True, null=True, verbose_name="العمر")

    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="عنوان السكن")
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name="المدينة")
    contact_number = models.CharField(max_length=14, blank=True, null=True, validators=[onlynumbers], verbose_name="رقم الهاتف")

    last_contact_date = models.DateTimeField(auto_now_add=False, blank=False, null=False, verbose_name="تاريخ الاختفاء")

    gender = models.CharField(max_length=10, null=False, blank=False, choices=Options.mafqood['gender'], verbose_name="الجنس")
    weight = models.IntegerField(blank=True, null=True, verbose_name="الوزن")
    height = models.IntegerField(blank=True, null=True, verbose_name="الطول")
    blod_type = models.CharField(max_length=10, null=True, blank=True, choices=Options.mafqood['blod_type'], verbose_name="فصيلة الدم")

    clothing = models.CharField(max_length=10, null=True, blank=True, verbose_name="ملابس")
    distinct_feature = models.CharField(max_length=255, blank=True, null=True, verbose_name="ملامح مميزة")
    any_other_details = models.TextField(blank=True, null=True, verbose_name="معلومات اضافية")
    photograph = models.ImageField(upload_to='mafqood', blank=True, null=True, verbose_name="صورة")

    # Contact person
    reporter_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="الاسم")
    reporter_surname = models.CharField(max_length=255, blank=True, null=True, verbose_name="اللقب")
    reporter_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="البريد الالكتروني")
    reporter_contact_number = models.CharField(max_length=14, blank=True, null=True, validators=[onlynumbers], verbose_name="رقم الهاتف")
    reporter_contact_number_2 = models.CharField(max_length=14, blank=True, null=True, validators=[onlynumbers], verbose_name="رقم الهاتف اضافي")
    reporter_relation_to_missing = models.CharField(max_length=255, blank=True, null=True, verbose_name="صلة القرابة للمفقود")
    reporter_city = models.CharField(max_length=255, blank=True, null=True, verbose_name="المدينة")
    reporter_address = models.CharField(max_length=255, blank=True, null=True, verbose_name="عنوان السكن")

    status = models.CharField(max_length=50, null=True, blank=True, choices=Options.mafqood['status'])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    @property
    def family(self):
        # Get list of all family members based on the Kutayib
        return self.citizens.order_by('-provider', 'date_of_birth')

    def calc_age(self):
        return (date.today() - self.date_of_birth) // timedelta(days=365.2425)

    def save(self, *args, **kwargs):
        if not self.pk and not self.age and self.date_of_birth:
            self.age = self.calc_age()
        return super(Mafqood, self).save(*args, **kwargs)