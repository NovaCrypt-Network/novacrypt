from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from Administration.models import Member
from Sponsors.models import Sponsor


def index(request):
    context = {
        "Teams":Team.objects.all(),
        "Projects":Project.objects.all(),
        "Members": Member.objects.count(),
        "Sponsors": Sponsor.objects.count()
    }
    return render(request, "Projects/index.html",context=context)

def TeamPage(request,TeamName):
    TeamThing = Team.objects.get(name=TeamName)
    context = {
        "Team":TeamThing,
        "Projects":Project.objects.filter(teams=Team.objects.get(name=TeamName)),
        "Leads":TeamThing.teamrole_set.all(),
        "Teams":Team.objects.all(),
        "Projects":TeamThing.project_set.all(),
        "Members": Member.objects.count(),
        "Sponsors": Sponsor.objects.count(),
        "TeamSlideshow": TeamSlideshowPicture.objects.filter(event=TeamThing).all()
    }
    return render(request,"Projects/TeamPage.html",context=context)

def ProjectPage(request,ProjectName):
    project = Project.objects.get(name=ProjectName)
    context = {
        "Project":project,
        "ProjectMembers":project.projectrole_set.all(),
        "Projects":Project.objects.all(),
        "Members": Member.objects.count(),
        "Sponsors": Sponsor.objects.count(),
        "ProjectSlideshow": ProjectSlideshowPicture.objects.filter(event=project).all()
    }
    return render(request,"Projects/ProjectPage.html",context=context)