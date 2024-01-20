# w pliku views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import DetailView, ListView

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
                if user.user.user_type == 'kierownik':
                    return redirect('userprofile_list')  # zamień 'home' na nazwę widoku, gdzie chcesz przekierować po zalogowaniu
                else:
                    return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('user_login')  # zamień 'login' na nazwę widoku, gdzie chcesz przekierować po wylogowaniu


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


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'user_detail.html'
    context_object_name = 'user_profile'


class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'list.html'  # Replace with your actual template name
    context_object_name = 'user_profiles'