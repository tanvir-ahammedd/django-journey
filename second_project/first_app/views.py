from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    return HttpResponse('''
                        <h1>This is from Contact Page</h1>
                        <a href = '/first_app/about/'>About</a>
                        <a href = '/second_app/feedback/'>feedback</a>
                        <a href = '/second_app/courses/'>courses</a>
                        ''')
def about(request):
    return HttpResponse('''
                        <h1>This is from About page</h1>
                        <a href = '/first_app/contact/'>Contact</a>
                        <a href = '/second_app/feedback/'>feedback</a>
                        <a href = '/second_app/courses/'>courses</a>
                        ''')

