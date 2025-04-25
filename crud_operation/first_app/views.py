from django.shortcuts import render, redirect
from .form import StudentForm
from .models import StudentModel

def home(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()
    return render(request, 'home.html', {'form': form})

def data(request):
    std = StudentModel.objects.all()
    return render(request, 'data.html', {'data': std})

def delete(request, roll):
    std = StudentModel.objects.get(pk=roll).delete()
    return redirect("datapage")
