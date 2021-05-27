from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    context = {
        "Subsidiaries":Subsidiary.objects.all(),
    }
    return render(request, "Subsidiaries/index.html",context=context)
