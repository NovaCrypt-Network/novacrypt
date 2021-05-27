import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.decorators.http import require_POST
#from Projects.models import Project, Team
from verify_email.email_handler import send_verification_email
from wagtail.users.models import UserProfile

from .decorators import allowed_users
from .forms import LoginForm, SignUpForm
from .models import Member
from .tokens import account_activation_token
from django.apps import apps
from Projects.models import Project
from Projects.models import Team
from .forms import UserUpdateForm,ProfileUpdateForm,ImageUpdateForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from mee6_py_api import API
from asgiref.sync import async_to_sync
import asyncio
import sys
import logging

@login_required(login_url='/Administration')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/Administration/dashboard')
        else:
            messages.error(request, 'Please correct the error(s) below.')
            messages.error(request, form.errors)
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Administration/change_password.html', {
        'form': form
    })



def append_side_views(request, context):
    if UserProfile.objects.filter(user=request.user).exists():
        context["Writer"] = UserProfile.objects.get(user=request.user)
    if request.user.groups.filter(name="EventManagers").exists():
        context["EventManager"] = True
    return context

# Create your views here.
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                #inactive_user = send_verification_email(request, form)
                #Person = Member(user=inactive_user)
                #Person.save()
                #return redirect('Administration:login')
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                Person = Member(user=user)
                Person.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your Novacrypt account.'
                message = render_to_string('Administration/email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                            mail_subject, message, to=[to_email]
                )
                email.send()
                return render(request,'Administration/password_approve_sent.html')

            else:
                context = {
                    'form':form,
                }
                return render(request,'Administration/signup.html',context=context)
        else:
            context = {
                'form':SignUpForm(),
            }
            return render(request,'Administration/signup.html',context=context)
    else:
        return redirect('Landing:index')



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request,'Administration/password_approve_done.html')
    else:
        return HttpResponse('Activation link is invalid!')


        
def login_request(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('Landing:index')
                else:
                    context = {
                        'form':form,
                        'signup':False
                    }
                    return render(request,'Administration/login.html',context=context)
            else:
                context = {
                        'form':form,
                        'signup':False
                    }
                return render(request,'Administration/login.html',context=context)
        else:
            context = {
                'form':LoginForm(),
                'signup':False
            }
            return render(request,'Administration/login.html',context=context)
    else:
        return redirect('Landing:index')

def logout_request(request):
    logout(request)
    return redirect('Landing:index')


@login_required(login_url='/Administration')
def dashboard(request):
    member = Member.objects.get(user=request.user)
    
    xp = member.xp

    teams = member.team_set.all()
    project1=[]

    for team in teams:
       project1.append(team.project_set.all())

    level = int(xp/500)
    context1={
        "Profile":member,
        "Teams":teams,
        "Projects":project1[0].all().distinct() if len(project1)>0 else "",
        "level":level,
        "levelp1":level+1,
        "levelper":int(((xp/500)-int(xp/500))*100),

    }
    
    return render(request,"Administration/Dashboard/dashboard.html", context=context1)

@login_required(login_url='/Administration')
def activity(request):
    Profile = Member.objects.get(user=request.user)

    xp = Profile.xp
    teams = 1
    level = int(xp/500)
    if level > 10:
        teams+=1
    if level > 20:
        teams+=1
        teams+=int((level-20)/5)
    if level > 50:
        teams='Unlimited'
    
    context={
        "Profile":Profile,
        "xp":xp,
        "level":level,
        "levelm1":int(xp/500)-1,
        "levelper":int(((xp/500)-int(xp/500))*100),
        "levelp1":int(xp/500)+1,
        "teams":teams
        
    }
    context = append_side_views(request,context)
    return render(request,"Administration/Dashboard/activity.html",context=context)



def profile_external(request, name):
    user = User.objects.get(username=name)
    Profile = Member.objects.get(user=user)
    xp = Profile.xp
    level = int(xp/500)
    teams = Profile.team_set.all()
    project1=[]

    for team in teams:
       project1.append(team.project_set.all())
    context={
            "Profile":Profile,
            "Teams":teams,
            "Projects":project1[0].all().distinct() if len(project1)>0 else "",
            "level":level,
            "levelp1":level+1,
            "levelper":int(((xp/500)-int(xp/500))*100),
            
        }
    return render(request, 'Administration/Dashboard/external_profile.html',context )

@login_required(login_url='/Administration')
def profile(request):
    if request.method == 'POST':
        Profile = Member.objects.get(user=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=Profile)
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p1_form = ImageUpdateForm(request.POST,request.FILES,instance=Profile)
        if 'acct' in request.POST:
            if p_form.is_valid() and u_form.is_valid():
                u_form.save()
                p_form.save()
                return redirect('Administration:profile')
        elif 'image' in request.POST:
            if(p1_form.is_valid()):
                p1_form.save()
                return redirect('Administration:profile')
    else:
        Profile = Member.objects.get(user=request.user)
        p_form = ProfileUpdateForm(instance=request.user)
        u_form = UserUpdateForm(instance=Profile)

    context={
        'p_form': p_form,
     'u_form': u_form,
      "Profile":Profile}
    return render(request, 'Administration/Dashboard/profile.html',context )