from django.contrib import admin
from volunteer.models import Volunteer, Team


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email_address', 'contact_number', 'status', 'assigned_team', 'created_user', 'created')
    search_fields = ['name', 'surname', 'assigned_team']

    def created_user(self, obj):
        return obj.is_current_user


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created')


admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Team, TeamAdmin)
