from django.urls import path
from . import views

app_name = 'Partners'
urlpatterns = [
    path('', views.index, name='index'),
]