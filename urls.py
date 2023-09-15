"""Mafqoodly URL Configuration"""
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from disaster import views as disaster_views
from mafqood import views as mafqood_views

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
admin.site.site_header = 'Mafqood - Admin'
admin.site.index_title = 'Mafqood.ly'


urlpatterns = [

    # favicon
    re_path(r'^favicon\.ico$', favicon_view),

    # Django Admin
    path('admin/', admin.site.urls),

    # LOGIN
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', disaster_views.disaster),

    # Disaster
    path('', disaster_views.disaster, name='main'),
    path('disaster/<int:disaster>', disaster_views.disaster, name='view_disaster'),

    # Mafqood
    path('disaster/<int:disaster>/mafqood/report_missing', mafqood_views.report_missing, name='report_missing'),

    # Person
    path('disaster/<int:disaster>/person/report_new_person', mafqood_views.report_new_person, name='report_new_person'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)