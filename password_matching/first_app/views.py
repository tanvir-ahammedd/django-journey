from django.shortcuts import render
from . forms import PasswordValidation
# Create your views here.
def home(request):
    return render(request, 'first_app/home.html')

def about(request):
    return render(request, 'first_app/about.html')


def password(request):
    if request.method == 'POST':
        form = PasswordValidation(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidation()
    return render(request, 'first_app/django_form.html', {'form':form})
       