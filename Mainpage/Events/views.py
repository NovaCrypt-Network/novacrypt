from datetime import time
from django.shortcuts import render
from .models import *
from django.utils import timezone
# Create your views here.
from itertools import chain


def index(request):
    comp = Competition.objects.filter(date__gt=timezone.now())
    web = Webinar.objects.filter(date__gt=timezone.now())
    event_list = sorted(
        chain(comp, web),
        key=lambda test: test.date, reverse=False)
    context = {
        "Events":event_list,
    }
    return render(request, "Events/index.html",context=context)

def infowebinar(request,name):
    context = {
        "Event":Webinar.objects.filter(title=name).first(),
    }
    return render(request, "Events/info_comp.html",context=context)



def comp(request, name):
    comps = Competition.objects.all()
    comp = Competition.objects.filter(title=name).first()
    slideshow = CompetitionSlideshowPicture.objects.filter(event=comp).all()
    faq = FAQ.objects.filter(event=comp).all()
    schedule = Schedule.objects.filter(event=comp).all()
    prize = Prize.objects.filter(event=comp).all()
    judges = Judge.objects.filter(competition=comp).all()
    #web = Webinar.objects.all()
    event_list = sorted(
        chain(comps),
        key=lambda test: test.date, reverse=True)
    context1 = {
        "EventSlideshow":slideshow,
        "Event":comp,
        "Events":event_list[:10],
        "FAQ":faq,
        "Schedule":schedule,
        "Prizes":prize,
        "Judges":judges
    }
    return render(request, "Events/comp.html",context=context1)


def webinar(request, name):
    
    webs = Webinar.objects.all()

    web = Webinar.objects.filter(title=name).first()

    slideshow = WebinarSlideshowPicture.objects.filter(event=web).all()

    speaker = Speaker.objects.all()


    event_list = sorted(
        chain(webs),
        key=lambda test: test.date, reverse=True)
    context1 = {
        "EventSlideshow":slideshow,
        "Webinar":web,
        "Webinars":event_list[:10],
        "Speakers":speaker,
        
    }
    return render(request, "Events/webinar.html",context=context1)


def all_comp(request):
    comp = Competition.objects.filter()
    event_list = sorted(
        chain(comp),
        key=lambda test: test.date, reverse=False)
    context = {
        "Events":event_list,
    }
    return render(request, "Events/all_comp.html",context=context)
    