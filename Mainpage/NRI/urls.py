from django.urls import path

from . import views

app_name = 'NRI'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:CourseID>/',views.course,name='Course'),
    
]