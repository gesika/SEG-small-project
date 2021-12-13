from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from clubs.forms import LogInForm, SignUpForm

# Create your views here.
def feed_applicant(request):
    return render(request, 'feed_applicant.html')

def feed_member(request):
    return render(request, 'feed_member.html')

def feed_officer(request):
    return render(request, 'feed_officer.html')

def feed_owner(request):
    return render(request, 'feed_owner.html')


def log_in(request):
    if request.method == 'POST':
        form = LogInForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_member:
                    return redirect('feed_member')
                elif user.is_officer:
                    return redirect('feed_officer')
                elif user.is_owner:
                    return redirect('feed_owner')
                else:
                    return redirect('feed_applicant')
        messages.add_message(request, messages.ERROR, "The credentials provided were invalid")
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form})

"""def log_in(request):
    if request.method == 'POST':
        form = LogInForm(data=request.POST)
        next = request.POST.get('next') or ''
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            member = authenticate(email=email, password=password)
            if member is not None:
                login(request, member)
                redirect_url = next or 'feed'
                return redirect(redirect_url)
        messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    else:
        next = request.GET.get('next') or ''
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form, 'next': next})"""

def log_out(request):
    logout(request)
    return redirect('home')

def home(request):
    return render (request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed_applicant')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})