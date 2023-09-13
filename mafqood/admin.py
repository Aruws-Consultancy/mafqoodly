from django.contrib import admin
from mafqood.models import Mafqood


class MafqoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'status', 'created')


admin.site.register(Mafqood, MafqoodAdmin)
