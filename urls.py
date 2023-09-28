"""Mafqoodly URL Configuration"""
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from disaster import views as disaster_views
from mafqood import views as mafqood_views
from volunteer import views as volunteer_views
from pages import views as static_pages_views

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
admin.site.site_header = 'Mafqood - Admin'
admin.site.index_title = 'Mafqood.ly'

handler404 = 'disaster.views.error_404'
handler500 = 'disaster.views.error_500'
handler403 = 'disaster.views.error_403'
handler400 = 'disaster.views.error_404'

urlpatterns = [

    # favicon
    re_path(r'^favicon\.ico$', favicon_view),

    # Django Admin
    path('admin/', admin.site.urls),

    # LOGIN
    path('accounts/', include('django.contrib.auth.urls')),

    # Disaster
    path('', disaster_views.disaster, name='main'),
    path('disaster/<int:disaster>', disaster_views.disaster, name='view_disaster'),

    # Mafqood
    path('disaster/<int:disaster>/mafqood/report_missing', mafqood_views.report_missing, name='report_missing'),
    path('disaster/<int:disaster>/mafqood/dashboard', mafqood_views.missing_dashboard, name='missing_dashboard'),
    path('disaster/<int:disaster>/mafqood/search', mafqood_views.mafqood_search, name='mafqood_search'),
    path('disaster/<int:disaster>/mafqood/<int:id>', mafqood_views.mafqood_update, name='mafqood_update'),

    # Person
    path('disaster/<int:disaster>/person/report_new_person', mafqood_views.report_new_person, name='report_new_person'),

    # Volunteer
    path('volunteer/new_volunteer', volunteer_views.new_volunteer, name='new_volunteer'),

    # Static Pages
    path('media', static_pages_views.media, name='media'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)