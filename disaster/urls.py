from django.urls import path

from disaster import views

app_name = 'disaster'

urlpatterns = [
    path('', views.disaster, name='main'),
    path('<slug:disaster>', views.disaster, name='view_disaster'),
]
