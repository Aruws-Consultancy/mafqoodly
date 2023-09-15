from django.db import models


class Disaster(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    image = models.ImageField(upload_to='disaster', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_main_focus = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    closed = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def missing_count(self):
        return self.missings.all().count()
