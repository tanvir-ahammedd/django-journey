from django.shortcuts import render, redirect
from .forms import RegisterForm, CustomPasswordChangeForm, CustomSetPasswordForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account Created Successfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('profile_page')

def loginuser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name, password = userpass)
                
                if user is not None:
                    login(request, user)
                    return redirect('profile_page')
        
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile_page')
    
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('login_page')

def user_logout(request):
    logout(request)
    return redirect('login_page')

def changePass(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile_page')
    else:
        form = CustomPasswordChangeForm(user=request.user)       
    return render(request, 'passchange.html', {'form': form})

def changePass2(request):
    if request.method == 'POST':
        form = CustomSetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile_page')
    else:
        form = CustomSetPasswordForm(user=request.user)       
    return render(request, 'passchange.html', {'form': form})
    