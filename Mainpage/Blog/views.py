from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import BlogPage
from wagtail.users.models import UserProfile
from django.contrib.auth.models import User
from Administration.models import Member
from django.views.decorators.http import require_POST
from django.core import serializers


def index(request):
    Response = BlogPage.objects.live().public().order_by('-first_published_at')[:19]
    context = {
        "Primary":Response[0],
        "Blogs":Response[1:]
    }
    return render(request, 'Blog/blog_index.html',context=context)
def Article(request, slug):
    page = BlogPage.objects.live().public().get(slug=slug)
    context = {
        "User":UserProfile.objects.get(user=page.owner),
        "page":page
    }
    page.views += 1
    page.save()
    return render(request,'Blog/blog_page.html',context=context)
@require_POST
def ArticleAPI(request):
    primary_key = request.POST.get('id')
    #a version of 0 means index blog page.
    if request.POST.get("version") == "0":
        BlogJson = [{"pk":Blog.pk,"thumbnail_url":Blog.thumbnail.url,"thumbnail_desc":Blog.thumbnail_desc,"slug":Blog.slug,"title":Blog.title,"username":Blog.owner.username,"first_name":Blog.owner.first_name.title(),"last_name":Blog.owner.last_name.title(),"publish":Blog.first_published_at,"category":Blog.category,"short_description":Blog.short_description} for Blog in BlogPage.objects.live().public().filter(id__lt=primary_key).order_by("-id")[:18]]
        data = {"BlogObjects":BlogJson}
        return JsonResponse(data)
    #a version of 1 means a category page.
    elif request.POST.get("version") == "1":
        category_input = request.POST.get("category")
        BlogJson = [{"pk":Blog.pk,"thumbnail_url":Blog.thumbnail.url,"thumbnail_desc":Blog.thumbnail_desc,"slug":Blog.slug,"title":Blog.title,"username":Blog.owner.username,"first_name":Blog.owner.first_name.title(),"last_name":Blog.owner.last_name.title(),"publish":Blog.first_published_at,"category":Blog.category,"short_description":Blog.short_description} for Blog in BlogPage.objects.live().public().filter(category=category_input).filter(id__lt=primary_key).order_by("-id")[:18]]
        data = {"BlogObjects":BlogJson}
        return JsonResponse(data)
    elif request.POST.get("version") == "2":
        author_input = request.POST.get("author")
        Profile = User.objects.get(username=author_input)
        BlogJson = [{"pk":Blog.pk,"thumbnail_url":Blog.thumbnail.url,"thumbnail_desc":Blog.thumbnail_desc,"slug":Blog.slug,"title":Blog.title,"username":Blog.owner.username,"first_name":Blog.owner.first_name.title(),"last_name":Blog.owner.last_name.title(),"publish":Blog.first_published_at,"category":Blog.category,"short_description":Blog.short_description} for Blog in BlogPage.objects.live().public().filter(owner=Profile).filter(id__lt=primary_key).order_by("-id")[:18]]
        data = {"BlogObjects":BlogJson}
        return JsonResponse(data)

def Category(request, cat):
    Response = BlogPage.objects.live().public().filter(category=cat).order_by('-first_published_at')[:18]
    context = {
        "Blogs":Response,
        "Category":cat
    }
    return render(request, 'Blog/blog_category.html',context=context)
def Author(request,username):
    Profile = User.objects.get(username=username)
    context = {
        "UserMember": Member.objects.get(user=Profile),
        "User":UserProfile.objects.get(user=Profile),
        "Blogs":BlogPage.objects.live().public().filter(owner=Profile).order_by('-first_published_at')[:18]
    }
    return render(request, 'Blog/blog_author.html',context=context)