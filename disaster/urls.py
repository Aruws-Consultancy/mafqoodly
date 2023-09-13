from django.urls import path, include

from disaster import views

app_name = 'disaster'

urlpatterns = [
    path('', views.disaster, name='main'),
    path('disaster/<int:disaster>', views.disaster, name='view_disaster'),
    path('disaster/<int:disaster>/mafqood/', include('mafqood.urls', namespace='mafqood')),
]
