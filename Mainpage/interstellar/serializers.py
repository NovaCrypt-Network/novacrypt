from .models import *
from rest_framework import serializers


class Competition_Tag_Serializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, value):
         return value.tag

    class Meta:
        model = Competition_Tag
        fields = ['tag']

class Funding_Tag_Serializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, value):
         return value.tag
    class Meta:
        model = Funding_Tag
        fields = ['tag']

class Opportunity_Tag_Serializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, value):
         return value.tag
    class Meta:
        model = Opportunity_Tag
        fields = ['tag']

class Internship_Tag_Serializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, value):
         return value.tag
    class Meta:
        model = Internship_Tag
        fields = ['tag']






class Competition_Serializer(serializers.HyperlinkedModelSerializer):
    tags = Competition_Tag_Serializer(read_only=True, many=True)
    class Meta:        
        
        model = Competition
        fields = ['id', 'name', 'logo', 'description', 'link', 'tags']


class Funding_Serializer(serializers.HyperlinkedModelSerializer):
    tags = Funding_Tag_Serializer(read_only=True, many=True)
    class Meta:
        
        model = Funding
        fields = ['id', 'name', 'amount', 'description', 'duedate' , 'type', 'link', 'tags']


class Opportunity_Serializer(serializers.HyperlinkedModelSerializer):
    tags = Opportunity_Tag_Serializer(read_only=True, many=True)
    class Meta:
        
        model = Opportunity
        fields = ['id', 'name', 'logo', 'description', 'link', 'tags']


class Internship_Serializer(serializers.HyperlinkedModelSerializer):
    tags = Internship_Tag_Serializer(read_only=True, many=True)
    class Meta:
        
        model = Internship
        fields = ['id', 'name', 'logo', 'description', 'link', 'tags']




