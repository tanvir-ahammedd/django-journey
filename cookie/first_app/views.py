from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def home(request):
    response = render(request, 'home.html')
    #these two types cookie will delete after closing the browser
    response.set_cookie('name', 'rahim')
    response.set_cookie('name', 'karim', max_age=10) #after 10 seconds cookie will be delete
    #cookie will not delete after closing the browser
    response.set_cookie('name', 'Hamin', expires=datetime.utcnow()+timedelta(days=7)) #set for 7 days
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name': name})

def delete_cookie(request):
    response = render(request, 'delete.html')
    response.delete_cookie('name')
    return response
