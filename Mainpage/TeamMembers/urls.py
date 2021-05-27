from django.urls import path
from . import views

app_name = 'TeamMembers'
urlpatterns = [
    path('', views.index, name='index'),
    path('managment', views.Management, name='Management'),
    path('webdev', views.WebDevelopment, name='WebDevelopment'),
    path('finance', views.Finance, name='Finance'),
    path('graphicdesign', views.GraphicDesign, name='GraphicDesign'),
    path('marketing', views.Marketing, name='Marketing'),
    path('hr', views.HumanResources, name='HumanResources'),
    path('writing', views.Writing, name='Writing'),
]