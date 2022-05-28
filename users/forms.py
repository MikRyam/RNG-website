from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

from django import forms
from django.forms import ModelForm, ValidationError
from .models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # widgets = {
        #     'username': TextInput(attrs={'class': 'form-control'}),
        # }


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))                            

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UpdateProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file', 'title': "Upload new profile image"}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style':"height: 100px", 'rows': 5}))
    position = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    linkedin_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    facebook_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    whatsapp_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    telegram_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    twitter_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    instagram_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) 

    class Meta:
        model = Profile
        fields = ['profile_image', 'bio', 'position', 'linkedin_url', 'facebook_url', 'whatsapp_url', 'telegram_url', 'twitter_url', 'instagram_url']
        


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
