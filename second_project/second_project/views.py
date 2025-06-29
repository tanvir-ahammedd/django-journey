from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>This is from Home</h1>')