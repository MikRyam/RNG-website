from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from users.models import Profile
from users.forms import SignUpForm, UpdateUserForm, UpdateProfileForm, MyPasswordChangeForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            # form.save()
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})



@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
                
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users:profile') 
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)        

    password_form = MyPasswordChangeForm(user=request.user, data=request.POST or None)
    if password_form.is_valid():
        password_form.save()
        update_session_auth_hash(request, password_form.user)
        messages.success(request, 'Your profile is updated successfully')
        return redirect(to='users:profile')
    
    profile = Profile.objects.filter(user=request.user)
        
    context={
        'profile': profile,       
        'user_form': user_form, 
        'profile_form': profile_form,
        'password_form': password_form,
    }

    return render(request, 'registration/profile.html', context)


