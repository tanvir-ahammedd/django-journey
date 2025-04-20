from django.shortcuts import render
from . forms import contactForm
from . forms import StudentData
# Create your views here.
def home(request):
    return render(request, 'first_app/home.html')

def about(request):
    return render(request, 'first_app/about.html')

def DjangoForm(request):
    form = contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'first_app/django_form.html', {'form': form})

def StudentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(request, 'first_app/django_form.html', {'form':form})
       