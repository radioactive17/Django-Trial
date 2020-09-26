from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from .models import EndUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import login as auth_login
import string
import random
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            image = form.cleaned_data['image']
            username = form.cleaned_data['username']
            user = User.objects.get(username = username)
            uid = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=6))
            enduser = EndUser(user = user, email = email, age = age, image = image, uid = uid)
            enduser.save()
            messages.success(request, f'Account created successfully')
            return redirect('Login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = User.objects.get(email = email).username
        password = request.POST.get('password')
        user = authenticate(request,username = username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Profile')
        else:
            return redirect('Login')
    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return redirect('Login')

@login_required
def profile(request):
    user = request.user
    enduser = EndUser.objects.get(user = user)
    return render(request, 'users/profile.html', {'enduser':enduser})
