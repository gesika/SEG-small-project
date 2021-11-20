from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from clubs.forms import SignUpForm

# Create your views here.

def feed(request):
    return render(request, 'feed.html')

def log_in(request):
    return render(request, 'log_in.html')

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            member = form.save()
            login(request, member)
            return redirect('feed')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})