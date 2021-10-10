from django.shortcuts import render
from NRI.models import *

# Create your views here.
def index(request):
    context = {
        "Courses": Course.objects.all(),
    }
    return render(request,"NRI/index.html",context=context)

def course(request, CourseID):
    context = {
        "Course": Course.objects.get(pk=CourseID),
        "Videos": Course.objects.get(pk=CourseID).videos.all(),
    }
    return render(request,"NRI/course.html",context=context)