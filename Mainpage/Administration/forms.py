from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible
from .models import *

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': "form-control",'type':'text','placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': "form-control",'type':'text','placeholder':'Last Name'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'class': "form-control",'type':'text','placeholder':'Email Address'}))
    captcha = ReCaptchaField()
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': 'form-control', 'placeholder': 'Verify Password'}))


    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control",'type':'text','placeholder':'Username'}),
        }
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'captcha')

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': "form-control",'type':'text','placeholder':'Username'}),
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control",'type':'password','placeholder':'Password'}))
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ('username','password','captcha')

class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model=Member
        fields=['avatar']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Member
        fields=['linkedin','instagram','github','bio','discordid']