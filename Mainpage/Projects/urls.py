from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Teams/<str:TeamName>/',views.TeamPage,name='TeamPage'),
    path('Projects/<str:ProjectName>/',views.ProjectPage,name="ProjectPage"),
]