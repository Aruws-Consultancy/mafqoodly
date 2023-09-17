from django.contrib import admin
from pages.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created')



admin.site.register(Page, PageAdmin)
