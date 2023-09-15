from django.contrib import admin
from volunteer.models import Volunteer


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email_address', 'status', 'created')


admin.site.register(Volunteer, VolunteerAdmin)
