from django.shortcuts import render, redirect
from . forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('login_page')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})

def loginuser(request):
    if request.method=='POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username=name, password = userpass)
            if user is not None:
                login(request, user)
                return redirect('profile_page')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('login_page')
        