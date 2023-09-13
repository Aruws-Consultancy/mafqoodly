from django.db import models
from datetime import date, timedelta
from config.constants import Options
from disaster.models import Disaster
from phone_field import PhoneField


class Mafqood(models.Model):

    disaster = models.ForeignKey(Disaster, related_name='missings', null=True, blank=True, on_delete=models.SET_NULL)

    # Missing Person
    first_name = models.CharField(max_length=255, blank=True, null=True)
    family_name = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    mother_name = models.CharField(max_length=255, blank=True, null=True)

    gender = models.CharField(max_length=10, null=True, blank=True, choices=Options.mafqood['gender'])

    date_of_birth = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    contact_number = PhoneField(blank=True, null=True)

    gender = models.CharField(max_length=10, null=True, blank=True, choices=Options.mafqood['gender'])
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    distinct_feature = models.CharField(max_length=255, blank=True, null=True)
    blod_type = models.CharField(max_length=10, null=True, blank=True, choices=Options.mafqood['blod_type'])

    last_contact_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    last_contact_details = models.CharField(max_length=255, blank=True, null=True)

    any_other_details = models.TextField(blank=True, null=True)

    photograph = models.ImageField(upload_to='mafqood', blank=True, null=True)

    # Contact person
    reporter_first_name = models.CharField(max_length=255, blank=True, null=True)
    reporter_last_name = models.CharField(max_length=255, blank=True, null=True)
    reporter_contact_number = PhoneField(blank=True, null=True)
    reporter_contact_number_2 = PhoneField(blank=True, null=True)
    reporter_relation_to_missing = models.CharField(max_length=255, blank=True, null=True)
    report_city = models.CharField(max_length=255, blank=True, null=True)
    report_address = models.CharField(max_length=255, blank=True, null=True)

    status = models.CharField(max_length=50, null=True, blank=True, choices=Options.mafqood['status'])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.family_name}'

    @property
    def family(self):
        # Get list of all family members based on the Kutayib
        return self.citizens.order_by('-provider', 'date_of_birth')

    def calc_age(self):
        date_for_age = date.today() if not self.date_of_death else self.date_of_death
        return (date_for_age - self.date_of_birth) // timedelta(days=365.2425)

    def save(self, *args, **kwargs):
        if not self.pk and not self.age and self.date_of_birth:
            self.age = self.calc_age()
        return super(Mafqood, self).save(*args, **kwargs)