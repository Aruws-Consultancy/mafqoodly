from django.contrib import admin
from volunteer.models import Volunteer, Team


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email_address', 'contact_number', 'status', 'assigned_team', 'created')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created')


admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Team, TeamAdmin)
