from django.contrib import admin
from disaster.models import Disaster


class DisasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'is_main_focus','created', 'closed')


admin.site.register(Disaster, DisasterAdmin)
