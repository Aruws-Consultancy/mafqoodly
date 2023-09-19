from django.db import models
from datetime import date, timedelta
from config.constants import Options
from disaster.models import Disaster
from django.core.validators import RegexValidator
import uuid

onlynumbers = RegexValidator(r'^[0-9]', 'Only numbers are allowed.')


class Mafqood(models.Model):

    disaster = models.ForeignKey(Disaster, related_name='missings', null=False, blank=False, on_delete=models.CASCADE)

    # Missing Person
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name="الاسم")
    father_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="اسم الاب")
    grandfather_name = models.CharField(max_length=255, blank=True, null=False, verbose_name="اسم الجد  (والد الأب)")
    surname = models.CharField(max_length=255, blank=False, null=False, verbose_name="اللقب")

    mother_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="اسم الام")

    date_of_birth = models.DateField(blank=True, null=True, verbose_name="تاريخ الميلاد")
    age = models.IntegerField(blank=True, null=True, verbose_name="العمر")

    nationality = models.CharField(max_length=255, null=True, blank=True, default='lby', choices=Options.countries, verbose_name="الجنسية")

    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="عنوان السكن")
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name="المدينة")
    contact_number = models.CharField(max_length=14, blank=True, null=True, validators=[onlynumbers], verbose_name="رقم الهاتف")

    last_contact_date = models.DateTimeField(auto_now_add=False, blank=False, null=False, verbose_name="تاريخ الاختفاء")

    gender = models.CharField(max_length=10, null=False, blank=False, choices=Options.general['gender'], verbose_name="الجنس")
    weight = models.IntegerField(blank=True, null=True, verbose_name="الوزن")
    height = models.IntegerField(blank=True, null=True, verbose_name="الطول")
    blod_type = models.CharField(max_length=10, null=True, blank=True, choices=Options.general['blod_type'], verbose_name="فصيلة الدم")

    clothing = models.CharField(max_length=10, null=True, blank=True, verbose_name="ملابس")
    distinct_feature = models.CharField(max_length=255, blank=True, null=True, verbose_name="ملامح مميزة")
    any_other_details = models.TextField(blank=True, null=True, verbose_name="معلومات اضافية")
    photograph = models.ImageField(upload_to='mafqoods', blank=True, null=True, verbose_name="صورة")

    # Reporter person
    reporter_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="الاسم")
    reporter_surname = models.CharField(max_length=255, blank=True, null=True, verbose_name="اللقب")
    reporter_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="البريد الالكتروني")
    reporter_contact_number = models.CharField(max_length=14, blank=True, null=True, validators=[onlynumbers], verbose_name="رقم الهاتف")
    reporter_contact_number_2 = models.CharField(max_length=14, blank=True, null=True, validators=[onlynumbers], verbose_name="رقم الهاتف اضافي")
    reporter_relation_to_missing = models.CharField(max_length=255, blank=True, null=True, verbose_name="صلة القرابة للمفقود")
    reporter_city = models.CharField(max_length=255, blank=True, null=True, verbose_name="المدينة")
    reporter_address = models.CharField(max_length=255, blank=True, null=True, verbose_name="عنوان السكن")

    # Status Update
    status = models.CharField(max_length=50, null=True, blank=True, default="missing", choices=Options.mafqood['status'])
    update_by = models.CharField(max_length=50, null=True, blank=True, choices=Options.mafqood['reporter'])
    update_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    matched_person = models.ForeignKey('Person', related_name='matched', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    @property
    def is_matched(self):
        return True if self.matched_person else False

    def calc_age(self):
        if not self.date_of_birth:
            return None
        return (date.today() - self.date_of_birth) // timedelta(days=365.2425)

    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.age and self.date_of_birth:
                self.age = self.calc_age()

            if self.photograph:
                self.photograph.name = f'{uuid.uuid4().hex[:6].upper()}_{self.photograph.name}'

        if self.pk is not None:
            orig = Mafqood.objects.get(pk=self.pk)
            if orig.photograph != self.photograph:
                self.photograph.name = f'{uuid.uuid4().hex[:6].upper()}_{self.photograph.name}'

        return super(Mafqood, self).save(*args, **kwargs)


class Person(models.Model):

    disaster = models.ForeignKey(Disaster, related_name='people', null=False, blank=False, on_delete=models.CASCADE)

    # Missing Person
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="الاسم")
    surname = models.CharField(max_length=255, blank=True, null=True, verbose_name="اللقب")

    nationality = models.CharField(max_length=255, null=True, blank=True, default='lby', choices=Options.countries, verbose_name="الجنسية")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="تاريخ الميلاد")
    age = models.IntegerField(blank=True, null=True, verbose_name="العمر")

    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="عنوان السكن")
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name="المدينة")
    contact_number = models.CharField(max_length=14, blank=True, null=True, validators=[onlynumbers], verbose_name="رقم الهاتف")

    current_location = models.CharField(max_length=255, blank=True, null=True, verbose_name="الموقع الحالي")

    gender = models.CharField(max_length=10, null=False, blank=False, choices=Options.general['gender'], verbose_name="الجنس")
    weight = models.IntegerField(blank=True, null=True, verbose_name="الوزن")
    height = models.IntegerField(blank=True, null=True, verbose_name="الطول")
    blod_type = models.CharField(max_length=10, null=True, blank=True, choices=Options.general['blod_type'], verbose_name="فصيلة الدم")

    clothing = models.CharField(max_length=10, null=True, blank=True, verbose_name="ملابس")
    distinct_feature = models.CharField(max_length=255, blank=True, null=True, verbose_name="ملامح مميزة")
    any_other_details = models.TextField(blank=True, null=True, verbose_name="معلومات اضافية")
    photograph = models.ImageField(upload_to='persons', blank=True, null=True, verbose_name="صورة")
    document = models.ImageField(upload_to='documents', blank=True, null=True, verbose_name="ملفات")

    status = models.CharField(max_length=50, null=True, blank=True, default="idp", choices=Options.people['status'], verbose_name="الوضع الحالي")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    @property
    def is_matched(self):
        return True if Mafqood.objects.filter(matched_person=self).count() > 1 else False

    def calc_age(self):
        return (date.today() - self.date_of_birth) // timedelta(days=365.2425)

    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.age and self.date_of_birth:
                self.age = self.calc_age()

            if self.photograph:
                self.photograph.name = f'{uuid.uuid4().hex[:6].upper()}_{self.photograph.name}'

        if self.pk is not None:
            orig = Person.objects.get(pk=self.pk)
            if orig.photograph != self.photograph:
                self.photograph.name = f'{uuid.uuid4().hex[:6].upper()}_{self.photograph.name}'

        return super(Person, self).save(*args, **kwargs)
