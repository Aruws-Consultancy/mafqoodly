from django.db import models
from datetime import date, timedelta
from config.constants import Options
from disaster.models import Disaster
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Mafqood(models.Model):
    disaster = models.ForeignKey(Disaster, related_name='missings', null=True, blank=True, on_delete=models.SET_NULL)

    first_name = models.CharField(max_length=255, blank=True, null=True)
    family_name = models.CharField(max_length=255, blank=True, null=True)

    father_name = models.CharField(max_length=255, blank=True, null=True)
    mother_name = models.CharField(max_length=255, blank=True, null=True)

    date_of_birth = models.DateField(blank=True, null=True)

    address = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    contact_number = models.IntegerField(blank=True, null=True)

    last_contact = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    last_contact_details = models.CharField(max_length=255, blank=True, null=True)

    any_other_details = models.TextField(blank=True, null=True)

    status = models.CharField(max_length=50, null=True, blank=True, choices=Options.mafqood['status'])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.father_name} {self.father_father_name} {self.family_name}'

    @property
    def age(self):
        date_for_age = date.today() if not self.date_of_death else self.date_of_death
        return (date_for_age - self.date_of_birth) // timedelta(days=365.2425)

    @property
    def family(self):
        # Get list of all family members based on the Kutayib
        return self.citizens.order_by('-provider', 'date_of_birth')

    def save(self, *args, **kwargs):
        if not self.pk:
            # Force NID to always be UPPER Case
            self.nid = self.nid.upper()
        return super(Mafqood, self).save(*args, **kwargs)
