from django.urls import path

from . import views

app_name = 'Landing'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('nri', views.nri, name='nri'),
    path('contact', views.contact, name='contact'),
    path('community', views.community, name='community'),
    path('community/CountryAPI',views.CountryAPI,name="CountryAPI"),
    path('community/ChapterAPI',views.ChapterAPI,name="ChapterAPI"),
    path('ssc-paper.html', views.roland_pdf, name='rolan5d_pdf'),
    path('navigation/news',views.news,name="news"),
    path('navigation/services',views.services,name="services"),
    path('navigation/research',views.research,name="research"),
    path('navigation/subsidiaries',views.subsidiaries,name="subsidiaries"),
    
]