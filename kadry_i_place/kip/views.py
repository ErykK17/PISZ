# w pliku views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserLoginForm, UserRegistrationForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # zamień 'home' na nazwę widoku, gdzie chcesz przekierować po zalogowaniu
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')  # zamień 'login' na nazwę widoku, gdzie chcesz przekierować po wylogowaniu

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user_profile = UserProfile(user=user, user_type=form.cleaned_data['user_type'])
            user_profile.save()
            return redirect('user_login')  # zamień 'login' na nazwę widoku, gdzie chcesz przekierować po rejestracji
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    username = request.user.username
    return render(request, 'home.html', {'username': username})

