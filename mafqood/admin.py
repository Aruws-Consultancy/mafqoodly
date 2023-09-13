from django.contrib import admin
from mafqood.models import Mafqood


class MafqoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'family_name', 'status')


admin.site.register(Mafqood, MafqoodAdmin)
