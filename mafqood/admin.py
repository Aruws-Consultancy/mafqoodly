from django.contrib import admin
from mafqood.models import Mafqood, Person


class MafqoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age', 'city', 'status', 'matched', 'created')
    search_fields = ['name', 'surname']

    def matched(self, obj):
        return obj.is_matched


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age', 'city', 'status', 'matched', 'created')
    search_fields = ['name', 'surname']

    def matched(self, obj):
        return obj.is_matched


admin.site.register(Mafqood, MafqoodAdmin)
admin.site.register(Person, PersonAdmin)
