from django.contrib import admin
from mafqood.models import Mafqood


class MafqoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'nid', 'first_name', 'family_name', 'status')


admin.site.register(Mafqood, MafqoodAdmin)
