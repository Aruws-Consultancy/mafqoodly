from django.contrib import admin
from mafqood.models import Mafqood


class MafqoodAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'family_name', 'status', 'created')


admin.site.register(Mafqood, MafqoodAdmin)
