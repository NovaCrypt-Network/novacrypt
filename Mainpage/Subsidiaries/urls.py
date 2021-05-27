from django.urls import path
from . import views

app_name = 'Subsidiaries'
urlpatterns = [
    path('', views.index, name='index'),
]