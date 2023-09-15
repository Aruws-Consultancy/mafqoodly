from django.contrib import admin
from mafqood.models import Mafqood, Person


class MafqoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age', 'status', 'created')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age', 'status', 'created')


admin.site.register(Mafqood, MafqoodAdmin)
admin.site.register(Person, PersonAdmin)
