"""Mafqoodly URL Configuration"""
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [

    # favicon
    re_path(r'^favicon\.ico$', favicon_view),

    # Django Admin
    path('admin/', admin.site.urls),

    # pages
    path('', include('disaster.urls', namespace='disaster')),
    path('mafqood/', include('mafqood.urls', namespace='mafqood')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)