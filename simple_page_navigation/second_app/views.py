from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def courses(request):
    return HttpResponse('''
                        <h1>This is from courses page</h1>
                        <a href = '/second_app/feedback/'>feedback</a>
                        <a href = '/first_app/contact/'>Contact</a>
                        <a href = '/first_app/about/'>About</a>
                        ''')
def feedback(request):
    return HttpResponse('''
                        <h1>This is from feedback page</h1>
                        <a href = '/first_app/about/'>About</a>
                        <a href = '/first_app/contact/'>Contact</a>
                        <a href = '/second_app/courses/'>courses</a>
                        ''')