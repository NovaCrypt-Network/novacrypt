"""Mainpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('BlogEditor/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),

    path('',include("Landing.urls"),name="LandingIndex"),
    path('Administration/',include('Administration.urls'),name="Administration"),
    path('Projects/',include('Projects.urls'),name="Projects"),
    path('events/',include('Events.urls'),name="Events"),
    path('journal/',include('Blog.urls'),name="Blog"),
    path('community',include('CommunityChapters.urls'),name="Community"),
    path('partners/',include('Partners.urls'),name="Partners"),
    path('sponsors/',include('Sponsors.urls'),name="Sponsors"),
    path('subsidiaries/',include('Subsidiaries.urls'),name="Subsidiaries"),
    path('nri/',include('NRI.urls'),name="NRI"),
    path('announcement/',include('Announcements.urls'),name="Announcements"),
    path('teammembers/',include('TeamMembers.urls'),name="TeamMembers"),
    path('api/interstellar/',include('interstellar.urls'),name="Interstellar"),
    path('admin/', admin.site.urls),
    path('verification/', include('verify_email.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
