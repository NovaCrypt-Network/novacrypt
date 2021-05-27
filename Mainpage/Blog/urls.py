from django.urls import path
from . import views

app_name = 'Blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('Article/<str:slug>',views.Article,name="ArticlePage"),
    path('ArticleAPI',views.ArticleAPI,name="ArticleJSON"),
    path('Category/<str:cat>',views.Category,name="CategoryPage"),
    path('Author/<str:username>',views.Author,name="AuthorPage"),
]