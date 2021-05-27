from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Test2")
    #return render(request, 'Blog/blog_index.html',context=context)