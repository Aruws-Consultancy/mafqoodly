from django.urls import path

from mafqood import views

app_name = 'mafqood'

urlpatterns = [
    path('<int:id>', views.mafqood, name='view_mafqood'),
]
