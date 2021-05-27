from django.urls import path
from . import views

app_name = 'Events'
urlpatterns = [
    path('', views.index, name='index'),
    path('info/webinar/<str:name>', views.infowebinar, name='InfoWebinar'),
    path('info/competitions', views.all_comp, name='AllComp'),
    path('webinar/<str:name>', views.webinar, name='Webinar'),
    path('competition/<str:name>', views.comp, name='Competiton'),
]