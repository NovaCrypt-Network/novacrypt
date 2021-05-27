from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    context = {
        "Partners":Partner.objects.all(),
    }
    return render(request, "Partners/index.html",context=context)
