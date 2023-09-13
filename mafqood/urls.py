from django.urls import path

from mafqood import views

app_name = 'mafqood'

urlpatterns = [
    path('report', views.report_missing, name='report_missing'),
]
