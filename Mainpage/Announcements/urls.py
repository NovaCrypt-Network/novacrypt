from django.urls import path
from . import views

app_name = 'Announcements'
urlpatterns = [
    path('', views.index, name='index'),
]