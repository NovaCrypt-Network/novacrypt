from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.get_api_root_view().cls.__name__ = "Interstellar"
router.get_api_root_view().cls.__doc__ = "Read-only public Rest-API for Interstellar"
router.register(r'competition', views.Competition_ViewSet, basename='Competition')
router.register(r'competition_tags', views.Competition_Tag_ViewSet)
router.register(r'funding', views.Funding_ViewSet, basename='Funding')
router.register(r'funding_tags', views.Funding_Tag_ViewSet)
router.register(r'opportunity', views.Opportunity_ViewSet, basename='Opportunity')
router.register(r'opportunity_tags', views.Opportunity_Tag_ViewSet)
router.register(r'internship', views.Internship_ViewSet, basename='Internship')
router.register(r'internship_tags', views.Internship_Tag_ViewSet)



urlpatterns = [
    path('', include(router.urls))
 ]