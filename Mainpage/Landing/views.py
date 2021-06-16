from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Administration.models import Member
from Projects.models import Team,Project
from Sponsors.models import Sponsor
from CommunityChapters.models import Country, Chapter
from django.contrib.staticfiles.views import serve
import os
import Mainpage.settings as main
from django.views.decorators.http import require_POST
from django.core import serializers

def index(request):
    context1 = {
        "Members": Member.objects.count(),
        "Projects": Project.objects.count(),
        "Sponsors": Sponsor.objects.count(),
        "Teams": Team.objects.count()
    }
    return render(request,"Landing/index.html",context=context1)
def about(request):
    return render(request,"Landing/about.html")

def contact(request):
    return render(request,"Landing/contact.html")
def community(request):
    context1 = {
        "Members": Member.objects.count(),
        "Projects": Project.objects.count(),
        "Sponsors": Sponsor.objects.count(),
        "Teams": Team.objects.count(),
        "Countries": Country.objects.all().order_by('name')
    }
    return render(request,"Landing/community.html",context=context1)

def roland_pdf(request):
    test_file = open(os.path.join(main.BASE_DIR, "STATIC/Landing/files/ssc-paper.pdf" ), 'rb')
    response = HttpResponse(content=test_file)
    response['Content-Type'] = 'application/pdf'
    #response['Content-Disposition'] = 'attachment; filename="%s.pdf"' \
                                   # % 'ssc-paper'
    return response

@require_POST
def CountryAPI(request):
    CountryKey = request.POST.get('CountryID')
    data = serializers.serialize('json',Chapter.objects.filter(country=Country.objects.get(id=CountryKey)).order_by('name'),fields=["name","reigon"])
    return HttpResponse(data)

@require_POST
def ChapterAPI(request):
    ChapterKey = request.POST.get('ChapterID')
    ChapterObject = Chapter.objects.get(id=ChapterKey)
    data = {
        "country":ChapterObject.country.name,
        "reigon":ChapterObject.reigon,
        "name":ChapterObject.name,
        "president":ChapterObject.president,
        "email":ChapterObject.email
    }
    if ChapterObject.instagram:
        data+={"instagram":ChapterObject.instagram}
    if ChapterObject.website:
        data+={"instagram":ChapterObject.website}
    return JsonResponse(data)


def news(request):
    return render(request,"Landing/navigation/News.html")

def services(request):
    return render(request,"Landing/navigation/Services.html")

def research(request):
    return render(request,"Landing/navigation/Research.html")

def subsidiaries(request):
    return render(request,"Landing/navigation/Subsidiaries.html")
