from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *


class Competition_Tag_ViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Competition_Tag.objects.all()
    serializer_class = Competition_Tag_Serializer
    
class Funding_Tag_ViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Funding_Tag.objects.all()
    serializer_class = Funding_Tag_Serializer
    
class Opportunity_Tag_ViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Opportunity_Tag.objects.all()
    serializer_class = Opportunity_Tag_Serializer
    
class Internship_Tag_ViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Internship_Tag.objects.all()
    serializer_class = Internship_Tag_Serializer
    


class Competition_ViewSet(viewsets.ReadOnlyModelViewSet):

    def get_queryset(self):

        queryset = Competition.objects.all()
        tag = self.request.query_params.get('tag')
        if tag is not None:
            queryset = queryset.filter(tags__tag__iexact=tag)
        return queryset
    
    serializer_class =  Competition_Serializer

class Funding_ViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Funding.objects.all()
    serializer_class = Funding_Serializer

class Opportunity_ViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Opportunity.objects.all()
    serializer_class = Opportunity_Serializer
class Internship_ViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Internship.objects.all()
    serializer_class = Internship_Serializer
