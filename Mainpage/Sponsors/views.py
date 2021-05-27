from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    context = {
        "Sponsor":Sponsor.objects.all(),
    }
    return render(request, "Sponsors/index.html",context=context)

def support_us(request):
    return render(request, "Sponsors/support-us.html")
