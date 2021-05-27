from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    context = {
        "TeamMembers":TeamMember.objects.all(),
    }
    return render(request, "TeamMembers/index.html",context=context)

def Management(request):
    context = {
        "TeamMembers":TeamMember.objects.filter(branch="Management"),
    }
    return render(request, "TeamMembers/index.html",context=context)

def WebDevelopment(request):
    context = {
        "TeamMembers":TeamMember.objects.filter(branch="Web Development"),
    }
    return render(request, "TeamMembers/index.html",context=context)

def Finance(request):
    context = {
        "TeamMembers":TeamMember.objects.filter(branch="Finance"),
    }
    return render(request, "TeamMembers/index.html",context=context)

def GraphicDesign(request):
    context = {
        "TeamMembers":TeamMember.objects.filter(branch="Graphic Design"),
    }
    return render(request, "TeamMembers/index.html",context=context)

def Marketing(request):
    context = {
        "TeamMembers":TeamMember.objects.filter(branch="Marketing"),
    }
    return render(request, "TeamMembers/index.html",context=context)

def HumanResources(request):
    context = {
        "TeamMembers":TeamMember.objects.filter(branch="Human Resources"),
    }
    return render(request, "TeamMembers/index.html",context=context)

def Writing(request):
    context = {
        "TeamMembers":TeamMember.objects.filter(branch="Writing"),
    }
    return render(request, "TeamMembers/index.html",context=context)
