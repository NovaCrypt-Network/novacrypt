from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    context = {
        "Announcements":Announcement.objects.all(),
    }
    return render(request, "Announcements/index.html",context=context)
