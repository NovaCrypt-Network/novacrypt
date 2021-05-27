from django.urls import path
from . import views

app_name = 'Sponsors'
urlpatterns = [
    path('', views.index, name='index'),
    path('support_us', views.support_us, name='support_us'),
]