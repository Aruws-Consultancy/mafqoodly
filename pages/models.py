from django.db import models


class Page(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True, help_text='name to appear in url /pages/name')

    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='disaster', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    content = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


