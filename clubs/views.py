from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from clubs.forms import LogInForm, SignUpForm, UserForm, PasswordForm
from .models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

# Create your views here.
@login_required
def feed_applicant(request):
    return render(request, 'feed_applicant.html')

@login_required
def feed_member(request):
    return render(request, 'feed_member.html')

@login_required
def feed_officer(request):
    return render(request, 'feed_officer.html')

@login_required
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
    next = request.GET.get('next') or ''
    return render(request, 'log_in.html', {'form': form, 'next': next})

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

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

@login_required
def show_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return redirect('user_list')
    else:
        return render(request, 'show_user.html', {'user': user})


@login_required
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UserForm(instance=current_user, data=request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, "Profile updated!")
            form.save()
            return redirect('feed_applicant')
    else:
        form = UserForm(instance=current_user)
    return render(request, 'profile.html', {'form': form})

@login_required
def password(request):
    current_user = request.user
    if request.method == 'POST':
        form = PasswordForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            if check_password(password, current_user.password):
                new_password = form.cleaned_data.get('new_password')
                current_user.set_password(new_password)
                current_user.save()
                login(request, current_user)
                messages.add_message(request, messages.SUCCESS, "Password updated!")
                return redirect('feed')
    form = PasswordForm()
    return render(request, 'password.html', {'form': form})

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